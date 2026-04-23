import sqlite3

connection = sqlite3.connect('chemistry.db')
cur = connection.cursor()

# ===== INSERT REACTANTS =====
reactants_data = [
    ('Na', 'element'),
    ('Cl2', 'element'),
    ('H2', 'element'),
    ('O2', 'element'),
    ('C', 'element'),
    ('S', 'element'),
    ('Fe', 'element'),
    ('Mg', 'element'),
    ('P4', 'element'),
    ('Br2', 'element'),
]

for name, type_ in reactants_data:
    cur.execute("""
        INSERT OR IGNORE INTO Reactants (name, type)
        VALUES (?, ?)
    """, (name, type_))

# ===== INSERT PRODUCTS =====
products_data = [
    ('NaCl', 'compound', 'White'),
    ('H2O', 'compound', 'Colorless'),
    ('CO2', 'compound', 'Colorless'),
    ('MgO', 'compound', 'White'),
    ('Fe2O3', 'compound', 'Red-Brown'),
    ('SO2', 'compound', 'Colorless'),
    ('P2O5', 'compound', 'White'),
    ('NaBr', 'compound', 'White'),
    ('MgS', 'compound', 'Gray-White'),
    ('CS2', 'compound', 'Colorless'),
]

for name, type_, color in products_data:
    cur.execute("""
        INSERT OR IGNORE INTO Products (name, type, color)
        VALUES (?, ?, ?)
    """, (name, type_, color))

# ===== INSERT REACTIONS =====
reactions_data = [
    (1, 'Combination', '2Na + Cl2 → 2NaCl', 'Sodium reacts with chlorine gas'),
    (2, 'Combination', '2H2 + O2 → 2H2O', 'Hydrogen burns in oxygen'),
    (3, 'Combination', 'C + O2 → CO2', 'Carbon burns in oxygen'),
    (4, 'Combination', '2Mg + O2 → 2MgO', 'Magnesium burns in oxygen'),
    (5, 'Combination', '4Fe + 3O2 → 2Fe2O3', 'Iron burns to form iron oxide'),
    (6, 'Combination', 'S + O2 → SO2', 'Sulfur burns in oxygen'),
    (7, 'Combination', 'P4 + 5O2 → P2O5', 'Phosphorus burns in oxygen'),
    (8, 'Combination', '2Na + Br2 → 2NaBr', 'Sodium reacts with bromine'),
    (9, 'Combination', 'Mg + S → MgS', 'Magnesium reacts with sulfur'),
    (10, 'Combination', 'C + 2S → CS2', 'Carbon reacts with sulfur'),
]

for product_id, reaction_type, equation, description in reactions_data:
    cur.execute("""
        INSERT OR IGNORE INTO Reactions (product_id, reaction_type, equation, description)
        VALUES (?, ?, ?, ?)
    """, (product_id, reaction_type, equation, description))

# ===== INSERT REACTION_REACTANTS =====
reaction_reactants_data = [
    (1, 1, 2), (1, 2, 1),
    (2, 3, 2), (2, 4, 1),
    (3, 5, 1), (3, 4, 1),
    (4, 8, 2), (4, 4, 1),
    (5, 7, 4), (5, 4, 3),
    (6, 6, 1), (6, 4, 1),
    (7, 9, 1), (7, 4, 5),
    (8, 1, 2), (8, 10, 1),
    (9, 8, 1), (9, 6, 1),
    (10, 5, 1), (10, 6, 2),
]

for reaction_id, reactant_id, coefficient in reaction_reactants_data:
    cur.execute("""
        INSERT OR IGNORE INTO Reaction_Reactants (reaction_id, reactant_id, coefficient)
        VALUES (?, ?, ?)
    """, (reaction_id, reactant_id, coefficient))

# ===== INSERT COMPOUND COMPOSITION =====
compounds_data = [
    # NaCl
    ('NaCl', 'Na', 1),
    ('NaCl', 'Cl', 1),
    
    # H2O
    ('H2O', 'H', 2),
    ('H2O', 'O', 1),
    
    # CO2
    ('CO2', 'C', 1),
    ('CO2', 'O', 2),
    
    # MgO
    ('MgO', 'Mg', 1),
    ('MgO', 'O', 1),
    
    # Fe2O3
    ('Fe2O3', 'Fe', 2),
    ('Fe2O3', 'O', 3),
    
    # SO2
    ('SO2', 'S', 1),
    ('SO2', 'O', 2),
    
    # P2O5
    ('P2O5', 'P', 2),
    ('P2O5', 'O', 5),
    
    # NaBr
    ('NaBr', 'Na', 1),
    ('NaBr', 'Br', 1),
    
    # MgS
    ('MgS', 'Mg', 1),
    ('MgS', 'S', 1),
    
    # CS2
    ('CS2', 'C', 1),
    ('CS2', 'S', 2),
    
    # Diatomic molecules
    ('H2', 'H', 2),
    ('O2', 'O', 2),
    ('Cl2', 'Cl', 2),
    ('Br2', 'Br', 2),
    ('P4', 'P', 4),
]

for compound_name, element_symbol, count in compounds_data:
    cur.execute("""
        INSERT OR IGNORE INTO Compound_Composition (compound_name, element_symbol, count)
        VALUES (?, ?, ?)
    """, (compound_name, element_symbol, count))

connection.commit()
connection.close()

print("✅ تم إدراج جميع البيانات بنجاح!")