import sqlite3

connection = sqlite3.connect('chemistry.db')
cur = connection.cursor()

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Hydrogen','H',1,1.008,'Gas','Colorless',-259.16,-252.87,
            0.08988,'Non-metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Helium','He',2,4.003,'Gas','Colorless',-272.2,-268.93,
            0.1785,'Noble Gas',0)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Lithium','Li',3,6.941,'Solid','Silver',180.54,1342,
            0.534,'Alkali Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Beryllium','Be',4,9.012,'Solid','Gray',1287,2471,
            1.848,'Alkaline Earth Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Boron','B',5,10.811,'Solid','Black',2076,3927,
            2.34,'Metalloid',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Carbon','C',6,12.011,'Solid','Black',3823,4827,
            2.267,'Non-metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Nitrogen','N',7,14.007,'Gas','Colorless',-210.0,-195.8,
            1.251,'Non-metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Oxygen','O',8,15.999,'Gas','Colorless',-218.3,-182.95,
            1.429,'Non-metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Fluorine','F',9,18.998,'Gas','Pale Yellow',-219.6,-188.1,
            1.696,'Halogen',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Neon','Ne',10,20.180,'Gas','Colorless',-248.6,-246.1,
            0.9002,'Noble Gas',0)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Sodium','Na',11,22.990,'Solid','Silver',97.72,883,
            0.971,'Alkali Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Magnesium','Mg',12,24.305,'Solid','Silver',650,1091,
            1.738,'Alkaline Earth Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Aluminum','Al',13,26.982,'Solid','Silver',660.3,2519,
            2.70,'Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Silicon','Si',14,28.086,'Solid','Gray',1414,3265,
            2.33,'Metalloid',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Phosphorus','P',15,30.974,'Solid','White',44.2,280.5,
            1.82,'Non-metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Sulfur','S',16,32.065,'Solid','Yellow',115.2,444.7,
            2.07,'Non-metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Chlorine','Cl',17,35.453,'Gas','Yellow-Green',-101.5,-34.04,
            3.214,'Halogen',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Argon','Ar',18,39.948,'Gas','Colorless',-189.3,-185.8,
            1.784,'Noble Gas',0)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Potassium','K',19,39.098,'Solid','Silver',63.5,774,
            0.862,'Alkali Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Calcium','Ca',20,40.078,'Solid','Silver',842,1484,
            1.55,'Alkaline Earth Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Scandium','Sc',21,44.956,'Solid','Silver',1541,2836,
            2.99,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Titanium','Ti',22,47.867,'Solid','Silver',1668,3287,
            4.506,'Transition Metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Vanadium','V',23,50.942,'Solid','Gray',1910,3407,
            6.11,'Transition Metal',5)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Chromium','Cr',24,51.996,'Solid','Gray',1907,2671,
            7.19,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Manganese','Mn',25,54.938,'Solid','Gray',1246,2061,
            7.44,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Iron','Fe',26,55.845,'Solid','Gray',1538,2862,
            7.874,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Cobalt','Co',27,58.933,'Solid','Gray',1495,2927,
            8.9,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Nickel','Ni',28,58.693,'Solid','Gray',1455,2913,
            8.908,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Copper','Cu',29,63.546,'Solid','Red',1085,2562,
            8.96,'Transition Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Zinc','Zn',30,65.380,'Solid','Gray',419.5,907,
            7.134,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Gallium','Ga',31,69.723,'Solid','Silver',29.76,2204,
            5.904,'Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Germanium','Ge',32,72.630,'Solid','Gray',938.3,2833,
            5.323,'Metalloid',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Arsenic','As',33,74.922,'Solid','Gray',817,614,
            5.75,'Metalloid',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Selenium','Se',34,78.971,'Solid','Red',221,685,
            4.79,'Non-metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Bromine','Br',35,79.904,'Liquid','Red-Brown',-7.2,58.8,
            3.12,'Halogen',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Krypton','Kr',36,83.798,'Gas','Colorless',-157.4,-153.2,
            3.749,'Noble Gas',0)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Rubidium','Rb',37,85.468,'Solid','Silver',39.3,688,
            1.532,'Alkali Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Strontium','Sr',38,87.62,'Solid','Silver',777,1382,
            2.64,'Alkaline Earth Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Yttrium','Y',39,88.906,'Solid','Silver',1526,3345,
            4.469,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Zirconium','Zr',40,91.224,'Solid','Gray',1855,4409,
            6.506,'Transition Metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Niobium','Nb',41,92.906,'Solid','Gray',2477,4744,
            8.57,'Transition Metal',5)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Molybdenum','Mo',42,95.95,'Solid','Gray',2623,4639,
            10.28,'Transition Metal',6)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Technetium','Tc',43,98.0,'Solid','Gray',2157,4265,
            11.5,'Transition Metal',7)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Ruthenium','Ru',44,101.07,'Solid','Gray',2334,4150,
            12.37,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Rhodium','Rh',45,102.91,'Solid','Gray',1966,3727,
            12.41,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Palladium','Pd',46,106.42,'Solid','Silver',1555,2963,
            12.02,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Silver','Ag',47,107.87,'Solid','Silver',961.8,2162,
            10.50,'Transition Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Cadmium','Cd',48,112.41,'Solid','Gray',321.1,765,
            8.65,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Indium','In',49,114.82,'Solid','Silver',156.6,2072,
            7.31,'Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Tin','Sn',50,118.71,'Solid','Silver',231.9,2602,
            7.287,'Metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Antimony','Sb',51,121.76,'Solid','Gray',630.7,1587,
            6.685,'Metalloid',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Tellurium','Te',52,127.60,'Solid','Gray',449.5,989.8,
            6.24,'Metalloid',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Iodine','I',53,126.90,'Solid','Gray',113.7,184.4,
            4.93,'Halogen',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Xenon','Xe',54,131.29,'Gas','Colorless',-111.8,-108.1,
            5.887,'Noble Gas',0)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Cesium','Cs',55,132.91,'Solid','Silver',28.4,669,
            1.873,'Alkali Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Barium','Ba',56,137.33,'Solid','Silver',727,1897,
            3.594,'Alkaline Earth Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Lanthanum','La',57,138.91,'Solid','Silver',920,3464,
            6.146,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Cerium','Ce',58,140.12,'Solid','Gray',798,3257,
            6.770,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Praseodymium','Pr',59,140.91,'Solid','Gray',931,3512,
            6.773,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Neodymium','Nd',60,144.24,'Solid','Gray',1021,3074,
            7.007,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Promethium','Pm',61,145.0,'Solid','Gray',1080,3000,
            7.26,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Samarium','Sm',62,150.36,'Solid','Gray',1072,1900,
            7.520,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Europium','Eu',63,151.96,'Solid','Gray',822,1596,
            5.243,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Gadolinium','Gd',64,157.25,'Solid','Gray',1313,3273,
            7.895,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Terbium','Tb',65,158.93,'Solid','Gray',1356,3123,
            8.229,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Dysprosium','Dy',66,162.50,'Solid','Gray',1412,2567,
            8.551,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Holmium','Ho',67,164.93,'Solid','Gray',1474,2695,
            8.795,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Erbium','Er',68,167.26,'Solid','Gray',1529,2863,
            9.066,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Thulium','Tm',69,168.93,'Solid','Gray',1545,1947,
            9.321,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Ytterbium','Yb',70,173.05,'Solid','Gray',819,1196,
            6.965,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Lutetium','Lu',71,174.97,'Solid','Gray',1663,3395,
            9.841,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Hafnium','Hf',72,178.49,'Solid','Gray',2233,4603,
            13.31,'Transition Metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Tantalum','Ta',73,180.95,'Solid','Gray',3017,5458,
            16.654,'Transition Metal',5)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Tungsten','W',74,183.84,'Solid','Gray',3422,5555,
            19.25,'Transition Metal',6)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Rhenium','Re',75,186.21,'Solid','Gray',3186,5596,
            21.02,'Transition Metal',7)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Osmium','Os',76,190.23,'Solid','Gray',3033,5012,
            22.59,'Transition Metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Iridium','Ir',77,192.22,'Solid','Gray',2466,4428,
            22.56,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Platinum','Pt',78,195.08,'Solid','Silver',1768.4,3825,
            21.45,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Gold','Au',79,196.97,'Solid','Yellow',1064.18,2856,
            19.30,'Transition Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Mercury','Hg',80,200.59,'Liquid','Silver',-38.83,356.73,
            13.5336,'Transition Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Thallium','Tl',81,204.38,'Solid','Silver',304,1457,
            11.85,'Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Lead','Pb',82,207.2,'Solid','Gray',327.5,1749,
            11.34,'Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Bismuth','Bi',83,208.98,'Solid','Gray',271.4,1564,
            9.807,'Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Polonium','Po',84,209.0,'Solid','Gray',254,962,
            9.32,'Metalloid',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Astatine','At',85,210.0,'Solid','Black',302,337,
            10.0,'Halogen',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Radon','Rn',86,222.0,'Gas','Colorless',-71,-61.7,
            9.73,'Noble Gas',0)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Francium','Fr',87,223.0,'Solid','Gray',8,677,
            2.48,'Alkali Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Radium','Ra',88,226.0,'Solid','Gray',700,1737,
            5.5,'Alkaline Earth Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Actinium','Ac',89,227.0,'Solid','Gray',1050,3200,
            10.07,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Thorium','Th',90,232.04,'Solid','Gray',1750,4820,
            11.72,'Transition Metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Protactinium','Pa',91,231.04,'Solid','Gray',1572,4000,
            15.37,'Transition Metal',5)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Uranium','U',92,238.03,'Solid','Gray',1135,4131,
            19.1,'Transition Metal',6)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Neptunium','Np',93,237.0,'Solid','Gray',644,3902,
            20.45,'Transition Metal',6)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Plutonium','Pu',94,244.0,'Solid','Gray',640,3228,
            19.84,'Transition Metal',6)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Americium','Am',95,243.0,'Solid','Gray',1176,2607,
            13.67,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Curium','Cm',96,247.0,'Solid','Gray',1345,3110,
            13.51,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Berkelium','Bk',97,247.0,'Solid','Gray',1259,2745,
            14.78,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Californium','Cf',98,251.0,'Solid','Gray',900,1173,
            15.1,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Einsteinium','Es',99,252.0,'Solid','Gray',860,996,
            13.5,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Fermium','Fm',100,257.0,'Solid','Gray',1527,NULL,
            NULL,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Mendelevium','Md',101,258.0,'Solid','Gray',827,1100,
            NULL,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Nobelium','No',102,259.0,'Solid','Gray',827,1100,
            NULL,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Lawrencium','Lr',103,262.0,'Solid','Gray',1627,NULL,
            NULL,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Rutherfordium','Rf',104,267.0,'Solid','Gray',2400,5800,
            NULL,'Transition Metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Dubnium','Db',105,268.0,'Solid','Gray',NULL,NULL,
            NULL,'Transition Metal',5)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Seaborgium','Sg',106,271.0,'Solid','Gray',NULL,NULL,
            NULL,'Transition Metal',6)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Bohrium','Bh',107,272.0,'Solid','Gray',NULL,NULL,
            NULL,'Transition Metal',7)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Hassium','Hs',108,270.0,'Solid','Gray',NULL,NULL,
            NULL,'Transition Metal',8)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Meitnerium','Mt',109,278.0,'Solid','Gray',NULL,NULL,
            NULL,'Transition Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Darmstadtium','Ds',110,281.0,'Solid','Gray',NULL,NULL,
            NULL,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Roentgenium','Rg',111,280.0,'Solid','Gray',NULL,NULL,
            NULL,'Transition Metal',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Copernicium','Cn',112,285.0,'Solid','Gray',NULL,NULL,
            NULL,'Transition Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Nihonium','Nh',113,286.0,'Solid','Gray',NULL,NULL,
            NULL,'Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Flerovium','Fl',114,289.0,'Solid','Gray',NULL,NULL,
            NULL,'Metal',4)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Moscovium','Mc',115,290.0,'Solid','Gray',NULL,NULL,
            NULL,'Metal',3)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Livermorium','Lv',116,293.0,'Solid','Gray',NULL,NULL,
            NULL,'Metal',2)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Tennessine','Ts',117,294.0,'Solid','Gray',NULL,NULL,
            NULL,'Halogen',1)
""")

cur.execute("""
    INSERT INTO Elements
            (name,symbol,atomic_num,atomic_weight,
            state,color,melting_point,boiling_point,
            density,classification,valence)
            
            VALUES('Oganesson','Og',118,294.0,'Gas','Colorless',NULL,NULL,
            NULL,'Noble Gas',0)
""")

connection.commit()
connection.close()

print("Data inserted")