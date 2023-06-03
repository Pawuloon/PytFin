import sqlite3 as sql
from datetime import datetime

from PythonFinalProj.Classes.Model.Meal import Meal


# Add retrival option when user will be entering products into his diet
class DataBase:
    def __init__(self):
        self.currentDate = datetime.now()
        self.conn = sql.connect('../Database/myDataBase.db')
        self.cursor = self.conn.cursor()
        self.execTable()

    # execute cursor for the table
    def execTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Product 
        (Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Name TEXT, Calories DECIMAL, Protein DECIMAL, Fat DECIMAL, Carbohydrates DECIMAL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Day 
                (Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                DayName Date, Calories DECIMAL, Protein DECIMAL, Fat DECIMAL, Carbohydrates DECIMAL)''')
        self.conn.commit()

    # execute addition
    def add(self, name, cal, protein, fat, carbs):
        self.cursor.execute("INSERT INTO Product (Name,Calories,Protein,Fat,Carbohydrates) "
                            "VALUES (?,?,?,?,?)", (name, cal, protein, fat, carbs))
        self.conn.commit()
        self.ditch()

    # Add day to database
    def addDay(self, Diet):
        self.cursor.execute("INSERT OR REPLACE INTO Day (DayName,Calories,Protein,Fat,Carbohydrates) "
                            "VALUES (?,?,?,?,?)", (Diet.dayName, Diet.calories, Diet.protein, Diet.fat, Diet.carbs))
        self.conn.commit()

    def replaceDay(self, Diet):
        self.cursor.execute("UPDATE Day SET Calories = ?, Protein = ?, Fat = ?, Carbohydrates = ? WHERE Id = ?",
                            (Diet.calories, Diet.protein, Diet.fat, Diet.carbs, self.cursor.lastrowid))
        self.conn.commit()

    # Ditch data that are incorrect
    def ditch(self):
        self.cursor.execute("DELETE FROM Product "
                            "WHERE Name='' OR Calories='' or Protein ='' or Fat ='' or Carbohydrates =''")
        self.conn.commit()

    def getDay(self):
        self.cursor.execute("SELECT DayName FROM Day order by Id desc limit 1")
        result = self.cursor.fetchone()
        return result

    # Retrive meals from database
    def getProducts(self):
        mealList = []
        myRes = self.cursor.execute("SELECT * FROM Product")
        rows = myRes.fetchall()

        for data in rows:
            Id = data[0]
            name = data[1]
            calories = data[2]
            protein = data[3]
            fat = data[4]
            carbs = data[5]
            meal = Meal(Id, name, calories, protein, fat, carbs)
            mealList.append(meal)

        return mealList
