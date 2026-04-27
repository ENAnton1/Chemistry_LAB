import sqlite3

connection = sqlite3.connect('chemistry.db')
cur = connection.cursor()

# ===== CREATE TABLE REACTANTS =====
cur.execute("""
    CREATE TABLE IF NOT EXISTS Reactants(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            type TEXT
    )
""")

# ===== CREATE TABLE PRODUCTS =====
cur.execute("""
    CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            type TEXT,
            color TEXT
    )
""")

# ===== CREATE TABLE REACTIONS =====
cur.execute("""
    CREATE TABLE IF NOT EXISTS Reactions(
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            reaction_type TEXT,
            equation TEXT,
            description TEXT,
            FOREIGN KEY(product_id) REFERENCES Products(id)
    )
""")

# ===== CREATE TABLE REACTION_REACTANTS =====
cur.execute("""
    CREATE TABLE IF NOT EXISTS Reaction_Reactants(
            id INTEGER PRIMARY KEY,
            reaction_id INTEGER,
            reactant_id INTEGER,
            coefficient INTEGER,
            FOREIGN KEY(reaction_id) REFERENCES Reactions(id),
            FOREIGN KEY(reactant_id) REFERENCES Reactants(id)
    )
""")

# ===== CREATE TABLE COMPOUND_COMPOSITION =====
cur.execute("""
    CREATE TABLE IF NOT EXISTS Compound_Composition(
            id INTEGER PRIMARY KEY,
            compound_name TEXT,
            element_symbol TEXT,
            count INTEGER,
            FOREIGN KEY(compound_name) REFERENCES Products(name)
    )
""")

connection.commit()
connection.close()

print("Table created")