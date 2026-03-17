import sqlite3

connection = sqlite3.connect('chemistry.db')
cur = connection.cursor()

cur.execute("""
    CREATE TABLE Elements(
            id INTEGER  PRIMARY KEY,
            name TEXT,
            symbol TEXT,
            atomic_num INTEGER,
            atomic_weight REAL ,
            state TEXT,
            color TEXT,
            melting_point REAL,
            boiling_point REAL,
            density REAL,
            classification TEXT,
            valence INTEGER  
            )
""")

connection.commit()
connection.close()

print("Table created succssufully")