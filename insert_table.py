import sqlite3

connection = sqlite3.connect('chemistry.db')
cur = connection.cursor()



# ====================== 1. INSERT REACTANTS (Elements + New Compounds) ======================
reactants_data = [
    ('Na', 'element'), ('Cl2', 'element'), ('H2', 'element'), ('O2', 'element'),
    ('C', 'element'), ('S', 'element'), ('Fe', 'element'), ('Mg', 'element'),
    ('P4', 'element'), ('Br2', 'element'),
    # New reactants for double displacement
    ('AgNO3', 'compound'), ('NaCl', 'compound'), ('BaCl2', 'compound'),
    ('K2CO3', 'compound'), ('Pb(NO3)2', 'compound'), ('KI', 'compound'),
    ('Na2SO4', 'compound'), ('CaCl2', 'compound'), ('Na3PO4', 'compound'),
    ('FeCl3', 'compound'), ('NaOH', 'compound'), ('ZnSO4', 'compound')
]

for name, typ in reactants_data:
    cur.execute("INSERT OR IGNORE INTO Reactants (name, type) VALUES (?, ?)", (name, typ))

# ====================== 2. INSERT PRODUCTS (Combination + Precipitates) ======================
products_data = [
    # Combination products (id 1-10)
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
    # Precipitates (id 11-20)
    ('AgCl', 'precipitate', 'White'),
    ('BaCO3', 'precipitate', 'White'),
    ('PbI2', 'precipitate', 'Yellow'),
    ('Ca3PO4', 'precipitate', 'White'),
    ('Fe(OH)3', 'precipitate', 'Reddish-Brown'),
    ('ZnOH', 'precipitate', 'White'),
    ('Ag2SO4', 'precipitate', 'White'),
    ('PbSO4', 'precipitate', 'White'),
    ('Ba3(PO4)2', 'precipitate', 'White'),
    ('AgI', 'precipitate', 'Yellow')
]

for name, typ, color in products_data:
    cur.execute("INSERT OR IGNORE INTO Products (name, type, color) VALUES (?, ?, ?)", (name, typ, color))

# ====================== 3. INSERT COMBINATION REACTIONS (product_id 1-10) ======================
combination_reactions = [
    (1, 'Combination', '2Na + Cl2 → 2NaCl', 'Sodium reacts with chlorine gas'),
    (2, 'Combination', '2H2 + O2 → 2H2O', 'Hydrogen burns in oxygen'),
    (3, 'Combination', 'C + O2 → CO2', 'Carbon burns in oxygen'),
    (4, 'Combination', '2Mg + O2 → 2MgO', 'Magnesium burns in oxygen'),
    (5, 'Combination', '4Fe + 3O2 → 2Fe2O3', 'Iron burns to form iron oxide'),
    (6, 'Combination', 'S + O2 → SO2', 'Sulfur burns in oxygen'),
    (7, 'Combination', 'P4 + 5O2 → P2O5', 'Phosphorus burns in oxygen'),
    (8, 'Combination', '2Na + Br2 → 2NaBr', 'Sodium reacts with bromine'),
    (9, 'Combination', 'Mg + S → MgS', 'Magnesium reacts with sulfur'),
    (10, 'Combination', 'C + 2S → CS2', 'Carbon reacts with sulfur')
]

for pid, rtype, eq, desc in combination_reactions:
    cur.execute("""
        INSERT OR IGNORE INTO Reactions (product_id, reaction_type, equation, description)
        VALUES (?, ?, ?, ?)
    """, (pid, rtype, eq, desc))

# ====================== 4. INSERT REACTION_REACTANTS FOR COMBINATION ======================
comb_rr = [
    (1,1,2),(1,2,1), (2,3,2),(2,4,1), (3,5,1),(3,4,1),
    (4,8,2),(4,4,1), (5,7,4),(5,4,3), (6,6,1),(6,4,1),
    (7,9,1),(7,4,5), (8,1,2),(8,10,1), (9,8,1),(9,6,1),
    (10,5,1),(10,6,2)
]

for rid, react_id, coeff in comb_rr:
    cur.execute("""
        INSERT OR IGNORE INTO Reaction_Reactants (reaction_id, reactant_id, coefficient)
        VALUES (?, ?, ?)
    """, (rid, react_id, coeff))

# ====================== 5. INSERT COMPOUND COMPOSITION (كل المركبات) ======================
all_composition = [
    # Original compounds
    ('NaCl', 'Na', 1), ('NaCl', 'Cl', 1),
    ('H2O', 'H', 2), ('H2O', 'O', 1),
    ('CO2', 'C', 1), ('CO2', 'O', 2),
    ('MgO', 'Mg', 1), ('MgO', 'O', 1),
    ('Fe2O3', 'Fe', 2), ('Fe2O3', 'O', 3),
    ('SO2', 'S', 1), ('SO2', 'O', 2),
    ('P2O5', 'P', 2), ('P2O5', 'O', 5),
    ('NaBr', 'Na', 1), ('NaBr', 'Br', 1),
    ('MgS', 'Mg', 1), ('MgS', 'S', 1),
    ('CS2', 'C', 1), ('CS2', 'S', 2),
    ('H2', 'H', 2), ('O2', 'O', 2), ('Cl2', 'Cl', 2),
    ('Br2', 'Br', 2), ('P4', 'P', 4),
    
    # New compounds + precipitates
    ('AgNO3', 'Ag', 1), ('AgNO3', 'N', 1), ('AgNO3', 'O', 3),
    ('BaCl2', 'Ba', 1), ('BaCl2', 'Cl', 2),
    ('K2CO3', 'K', 2), ('K2CO3', 'C', 1), ('K2CO3', 'O', 3),
    ('Pb(NO3)2', 'Pb', 1), ('Pb(NO3)2', 'N', 2), ('Pb(NO3)2', 'O', 6),
    ('KI', 'K', 1), ('KI', 'I', 1),
    ('Na2SO4', 'Na', 2), ('Na2SO4', 'S', 1), ('Na2SO4', 'O', 4),
    ('CaCl2', 'Ca', 1), ('CaCl2', 'Cl', 2),
    ('Na3PO4', 'Na', 3), ('Na3PO4', 'P', 1), ('Na3PO4', 'O', 4),
    ('FeCl3', 'Fe', 1), ('FeCl3', 'Cl', 3),
    ('NaOH', 'Na', 1), ('NaOH', 'O', 1), ('NaOH', 'H', 1),
    ('ZnSO4', 'Zn', 1), ('ZnSO4', 'S', 1), ('ZnSO4', 'O', 4),
    ('AgCl', 'Ag', 1), ('AgCl', 'Cl', 1),
    ('BaCO3', 'Ba', 1), ('BaCO3', 'C', 1), ('BaCO3', 'O', 3),
    ('PbI2', 'Pb', 1), ('PbI2', 'I', 2),
    ('Ca3PO4', 'Ca', 3), ('Ca3PO4', 'P', 1), ('Ca3PO4', 'O', 4),
    ('Fe(OH)3', 'Fe', 1), ('Fe(OH)3', 'O', 3), ('Fe(OH)3', 'H', 3),
    ('ZnOH', 'Zn', 1), ('ZnOH', 'O', 1), ('ZnOH', 'H', 1),
    ('Ag2SO4', 'Ag', 2), ('Ag2SO4', 'S', 1), ('Ag2SO4', 'O', 4),
    ('PbSO4', 'Pb', 1), ('PbSO4', 'S', 1), ('PbSO4', 'O', 4),
    ('Ba3(PO4)2', 'Ba', 3), ('Ba3(PO4)2', 'P', 2), ('Ba3(PO4)2', 'O', 8),
    ('AgI', 'Ag', 1), ('AgI', 'I', 1)
]

for name, elem, cnt in all_composition:
    cur.execute("""
        INSERT OR IGNORE INTO Compound_Composition (compound_name, element_symbol, count)
        VALUES (?, ?, ?)
    """, (name, elem, cnt))

# ====================== 6. INSERT DOUBLE DISPLACEMENT REACTIONS (product_id من 11 إلى 20) ======================
dd_reactions = [
    (11, 'Double Displacement', 'AgNO3 + NaCl → AgCl↓ + NaNO3', 'Silver nitrate reacts with sodium chloride forming white precipitate'),
    (12, 'Double Displacement', 'BaCl2 + K2CO3 → BaCO3↓ + 2KCl', 'Barium chloride reacts with potassium carbonate forming white precipitate'),
    (13, 'Double Displacement', 'Pb(NO3)2 + 2KI → PbI2↓ + 2KNO3', 'Lead nitrate reacts with potassium iodide forming yellow precipitate'),
    (14, 'Double Displacement', 'CaCl2 + Na3PO4 → Ca3(PO4)2↓ + 3NaCl', 'Calcium chloride reacts with sodium phosphate forming white precipitate'),
    (15, 'Double Displacement', 'FeCl3 + 3NaOH → Fe(OH)3↓ + 3NaCl', 'Iron(III) chloride reacts with sodium hydroxide forming reddish-brown precipitate'),
    (16, 'Double Displacement', 'ZnSO4 + 2NaOH → Zn(OH)2↓ + Na2SO4', 'Zinc sulfate reacts with sodium hydroxide forming white precipitate'),
    (17, 'Double Displacement', '2AgNO3 + Na2SO4 → Ag2SO4↓ + 2NaNO3', 'Silver nitrate reacts with sodium sulfate forming white precipitate'),
    (18, 'Double Displacement', 'Pb(NO3)2 + Na2SO4 → PbSO4↓ + 2NaNO3', 'Lead nitrate reacts with sodium sulfate forming white precipitate'),
    (19, 'Double Displacement', '3BaCl2 + Na3PO4 → Ba3(PO4)2↓ + 6NaCl', 'Barium chloride reacts with sodium phosphate forming white precipitate'),
    (20, 'Double Displacement', 'AgNO3 + KI → AgI↓ + KNO3', 'Silver nitrate reacts with potassium iodide forming yellow precipitate')
]

for pid, rtype, eq, desc in dd_reactions:
    cur.execute("""
        INSERT OR IGNORE INTO Reactions (product_id, reaction_type, equation, description)
        VALUES (?, ?, ?, ?)
    """, (pid, rtype, eq, desc))

# ====================== 7. INSERT REACTION_REACTANTS FOR DOUBLE DISPLACEMENT ======================
dd_reactants_data = [
    (11, 'AgNO3', 1), (11, 'NaCl', 1),
    (12, 'BaCl2', 1), (12, 'K2CO3', 1),
    (13, 'Pb(NO3)2', 1), (13, 'KI', 2),
    (14, 'CaCl2', 1), (14, 'Na3PO4', 1),
    (15, 'FeCl3', 1), (15, 'NaOH', 3),
    (16, 'ZnSO4', 1), (16, 'NaOH', 2),
    (17, 'AgNO3', 2), (17, 'Na2SO4', 1),
    (18, 'Pb(NO3)2', 1), (18, 'Na2SO4', 1),
    (19, 'BaCl2', 3), (19, 'Na3PO4', 1),
    (20, 'AgNO3', 1), (20, 'KI', 1)
]

for reaction_id, reactant_name, coefficient in dd_reactants_data:
    cur.execute("""
        INSERT OR IGNORE INTO Reaction_Reactants (reaction_id, reactant_id, coefficient)
        SELECT ?, id, ? FROM Reactants WHERE name = ?
    """, (reaction_id, coefficient, reactant_name))

connection.commit()
connection.close()

print("Data inserted")
