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
                Day TEXT, Calories DECIMAL, Protein DECIMAL, Fat DECIMAL, Carbohydrates DECIMAL)''')
        self.conn.commit()

    # execute addition
    def add(self, name, cal, protein, fat, carbs):
        self.cursor.execute("INSERT INTO Product (Name,Calories,Protein,Fat,Carbohydrates) "
                            "VALUES (?,?,?,?,?)", (name, cal, protein, fat, carbs))
        self.conn.commit()
        self.ditch()

    def addDay(self, Diet):
        self.cursor.execute("INSERT INTO Day (Day,Calories,Protein,Fat,Carbohydrates) "
                            "VALUES (?,?,?,?,?)", (Diet.dayName, Diet.calories, Diet.protein, Diet.fat, Diet.carbs))
        self.conn.commit()

    # Ditch data that are incorrect
    def ditch(self):
        self.cursor.execute("DELETE FROM Product "
                            "WHERE Name='' OR Calories='' or Protein ='' or Fat ='' or Carbohydrates =''")
        self.conn.commit()

    def clearDay(self):
        self.cursor.execute("DELETE FROM Day where Day ={}".format(self.currentDate.strftime("%d/%m/%Y")))
        self.conn.commit()

    # Retrive meals from database
    def getProducts(self):
        mealList = []
        myRes = self.cursor.execute("SELECT * FROM Product")
        rows = myRes.fetchall()

        for data in rows:
            id = data[0]
            name = data[1]
            calories = data[2]
            protein = data[3]
            fat = data[4]
            carbs = data[5]
            meal = Meal(id, name, calories, protein, fat, carbs)
            mealList.append(meal)

        return mealList
