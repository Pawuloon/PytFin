import sqlite3 as sql

from PythonFinalProj.Classes.Meal import Meal


# Add retrival option when user will be entering products into his diet
class DataBase:
    def __init__(self):
        self.conn = sql.connect('../Database/myDataBase.db')
        self.cursor = self.conn.cursor()
        self.execTable()

    # execute cursor for the table
    def execTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Product 
        (Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Name TEXT, Calories DECIMAL, Protein DECIMAL, Fat DECIMAL, Carbohydrates DECIMAL)''')
        self.conn.commit()

    # execute addition
    def add(self, name, cal, protein, fat, carbs):
        self.cursor.execute("INSERT INTO Product (Name,Calories,Protein,Fat,Carbohydrates) "
                            "VALUES (?,?,?,?,?)", (name, cal, protein, fat, carbs))
        self.conn.commit()
        self.ditch()

    def ditch(self):
        self.cursor.execute("DELETE FROM Product "
                            "WHERE Name='' OR Calories='' or Protein ='' or Fat ='' or Carbohydrates =''")
        self.conn.commit()

    def retrieve(self):
        mealList = []
        myRes = self.cursor.execute("SELECT * FROM Product")
        rows = myRes.fetchall()

        for data in rows:
            name = data[0]
            calories = data[1]
            protein = data[2]
            fat = data[3]
            carbs = data[4]
            meal = Meal(name, calories, protein, fat, carbs)
            mealList.append(meal)

        return mealList
