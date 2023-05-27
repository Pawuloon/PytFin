import sqlite3 as sql

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
