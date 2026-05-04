import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
from tkinter import Canvas
import random
import math
import re

class ChemistrySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("⚗️ Chemistry Experiment Simulator")
        self.root.geometry("1200x900")
        self.root.configure(bg='#f8f9fa')
        self.is_dark = False

        try:
            self.conn = sqlite3.connect('chemistry.db')
            self.cursor = self.conn.cursor()
            self._ensure_tables_exist()
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not connect to database: {e}")

        self.score = 0
        self.total_attempts = 0
        self.quiz_mode = False
        self.quiz_questions = []
        self.current_question = 0
        self.quiz_score = 0
        self.timer_id = None
        self.time_remaining = 0
        self.hints_used = 0
        self.max_hints = 3

        self.periodic_table = {
            'H':  {'name': 'Hydrogen', 'number': 1, 'mass': 1.008, 'group': 1, 'period': 1, 'category': 'Nonmetal', 'color': '#90EE90'},
            'He': {'name': 'Helium', 'number': 2, 'mass': 4.003, 'group': 18, 'period': 1, 'category': 'Noble Gas', 'color': '#FFB6C1'},
            'Li': {'name': 'Lithium', 'number': 3, 'mass': 6.941, 'group': 1, 'period': 2, 'category': 'Alkali Metal', 'color': '#FF6B6B'},
            'Be': {'name': 'Beryllium', 'number': 4, 'mass': 9.012, 'group': 2, 'period': 2, 'category': 'Alkaline Earth', 'color': '#FFE4B5'},
            'B':  {'name': 'Boron', 'number': 5, 'mass': 10.81, 'group': 13, 'period': 2, 'category': 'Metalloid', 'color': '#DDA0DD'},
            'C':  {'name': 'Carbon', 'number': 6, 'mass': 12.01, 'group': 14, 'period': 2, 'category': 'Nonmetal', 'color': '#90EE90'},
            'N':  {'name': 'Nitrogen', 'number': 7, 'mass': 14.01, 'group': 15, 'period': 2, 'category': 'Nonmetal', 'color': '#90EE90'},
            'O':  {'name': 'Oxygen', 'number': 8, 'mass': 16.00, 'group': 16, 'period': 2, 'category': 'Nonmetal', 'color': '#90EE90'},
            'F':  {'name': 'Fluorine', 'number': 9, 'mass': 19.00, 'group': 17, 'period': 2, 'category': 'Halogen', 'color': '#FFD700'},
            'Ne': {'name': 'Neon', 'number': 10, 'mass': 20.18, 'group': 18, 'period': 2, 'category': 'Noble Gas', 'color': '#FFB6C1'},
            'Na': {'name': 'Sodium', 'number': 11, 'mass': 22.99, 'group': 1, 'period': 3, 'category': 'Alkali Metal', 'color': '#FF6B6B'},
            'Mg': {'name': 'Magnesium', 'number': 12, 'mass': 24.31, 'group': 2, 'period': 3, 'category': 'Alkaline Earth', 'color': '#FFE4B5'},
            'Al': {'name': 'Aluminum', 'number': 13, 'mass': 26.98, 'group': 13, 'period': 3, 'category': 'Post-transition', 'color': '#B0C4DE'},
            'Si': {'name': 'Silicon', 'number': 14, 'mass': 28.09, 'group': 14, 'period': 3, 'category': 'Metalloid', 'color': '#DDA0DD'},
            'P':  {'name': 'Phosphorus', 'number': 15, 'mass': 30.97, 'group': 15, 'period': 3, 'category': 'Nonmetal', 'color': '#90EE90'},
            'S':  {'name': 'Sulfur', 'number': 16, 'mass': 32.07, 'group': 16, 'period': 3, 'category': 'Nonmetal', 'color': '#90EE90'},
            'Cl': {'name': 'Chlorine', 'number': 17, 'mass': 35.45, 'group': 17, 'period': 3, 'category': 'Halogen', 'color': '#FFD700'},
            'Ar': {'name': 'Argon', 'number': 18, 'mass': 39.95, 'group': 18, 'period': 3, 'category': 'Noble Gas', 'color': '#FFB6C1'},
            'K':  {'name': 'Potassium', 'number': 19, 'mass': 39.10, 'group': 1, 'period': 4, 'category': 'Alkali Metal', 'color': '#FF6B6B'},
            'Ca': {'name': 'Calcium', 'number': 20, 'mass': 40.08, 'group': 2, 'period': 4, 'category': 'Alkaline Earth', 'color': '#FFE4B5'},
            'Fe': {'name': 'Iron', 'number': 26, 'mass': 55.85, 'group': 8, 'period': 4, 'category': 'Transition Metal', 'color': '#87CEEB'},
            'Cu': {'name': 'Copper', 'number': 29, 'mass': 63.55, 'group': 11, 'period': 4, 'category': 'Transition Metal', 'color': '#87CEEB'},
            'Zn': {'name': 'Zinc', 'number': 30, 'mass': 65.38, 'group': 12, 'period': 4, 'category': 'Transition Metal', 'color': '#87CEEB'},
            'Ag': {'name': 'Silver', 'number': 47, 'mass': 107.9, 'group': 11, 'period': 5, 'category': 'Transition Metal', 'color': '#87CEEB'},
            'Au': {'name': 'Gold', 'number': 79, 'mass': 197.0, 'group': 11, 'period': 6, 'category': 'Transition Metal', 'color': '#87CEEB'},
            'Hg': {'name': 'Mercury', 'number': 80, 'mass': 200.6, 'group': 12, 'period': 6, 'category': 'Transition Metal', 'color': '#87CEEB'},
            'Pb': {'name': 'Lead', 'number': 82, 'mass': 207.2, 'group': 14, 'period': 6, 'category': 'Post-transition', 'color': '#B0C4DE'},
        }

        self.create_ui()

    def _ensure_tables_exist(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Elements (
                symbol TEXT PRIMARY KEY,
                name TEXT,
                atomic_number INTEGER,
                atomic_mass REAL,
                group_num INTEGER,
                period INTEGER,
                category TEXT
            )
        """)

        self.cursor.execute("SELECT COUNT(*) FROM Elements")
        if self.cursor.fetchone()[0] == 0:
            elements_data = [
                ('H', 'Hydrogen', 1, 1.008, 1, 1, 'Nonmetal'),
                ('He', 'Helium', 2, 4.003, 18, 1, 'Noble Gas'),
                ('Li', 'Lithium', 3, 6.941, 1, 2, 'Alkali Metal'),
                ('Be', 'Beryllium', 4, 9.012, 2, 2, 'Alkaline Earth'),
                ('B', 'Boron', 5, 10.81, 13, 2, 'Metalloid'),
                ('C', 'Carbon', 6, 12.01, 14, 2, 'Nonmetal'),
                ('N', 'Nitrogen', 7, 14.01, 15, 2, 'Nonmetal'),
                ('O', 'Oxygen', 8, 16.00, 16, 2, 'Nonmetal'),
                ('F', 'Fluorine', 9, 19.00, 17, 2, 'Halogen'),
                ('Ne', 'Neon', 10, 20.18, 18, 2, 'Noble Gas'),
                ('Na', 'Sodium', 11, 22.99, 1, 3, 'Alkali Metal'),
                ('Mg', 'Magnesium', 12, 24.31, 2, 3, 'Alkaline Earth'),
                ('Al', 'Aluminum', 13, 26.98, 13, 3, 'Post-transition'),
                ('Si', 'Silicon', 14, 28.09, 14, 3, 'Metalloid'),
                ('P', 'Phosphorus', 15, 30.97, 15, 3, 'Nonmetal'),
                ('S', 'Sulfur', 16, 32.07, 16, 3, 'Nonmetal'),
                ('Cl', 'Chlorine', 17, 35.45, 17, 3, 'Halogen'),
                ('Ar', 'Argon', 18, 39.95, 18, 3, 'Noble Gas'),
                ('K', 'Potassium', 19, 39.10, 1, 4, 'Alkali Metal'),
                ('Ca', 'Calcium', 20, 40.08, 2, 4, 'Alkaline Earth'),
                ('Fe', 'Iron', 26, 55.85, 8, 4, 'Transition Metal'),
                ('Cu', 'Copper', 29, 63.55, 11, 4, 'Transition Metal'),
                ('Zn', 'Zinc', 30, 65.38, 12, 4, 'Transition Metal'),
                ('Ag', 'Silver', 47, 107.9, 11, 5, 'Transition Metal'),
                ('Au', 'Gold', 79, 197.0, 11, 6, 'Transition Metal'),
                ('Hg', 'Mercury', 80, 200.6, 12, 6, 'Transition Metal'),
                ('Pb', 'Lead', 82, 207.2, 14, 6, 'Post-transition'),
            ]
            self.cursor.executemany(
                "INSERT INTO Elements (symbol, name, atomic_number, atomic_mass, group_num, period, category) VALUES (?, ?, ?, ?, ?, ?, ?)",
                elements_data
            )

        self.conn.commit()

    def create_ui(self):
        header_frame = tk.Frame(self.root, bg='#2563eb', height=110)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)

        title = tk.Label(header_frame, text="⚗️ Chemistry Experiment Simulator",
                        font=("Segoe UI", 28, "bold"), bg='#2563eb', fg='#ffffff')
        title.pack(pady=18)

        subtitle = tk.Label(header_frame, text="Balance Chemical Equations & Explore Reactions",
                            font=("Segoe UI", 12), bg='#2563eb', fg='#dbeafe')
        subtitle.pack()

        score_bar = tk.Frame(self.root, bg='#f1f5f9', height=40)
        score_bar.pack(fill=tk.X, padx=30, pady=(0, 5))
        score_bar.pack_propagate(False)

        self.score_label = tk.Label(score_bar, text="Score: 0 | Accuracy: 0%", 
                                   font=("Segoe UI", 12, "bold"), bg='#f1f5f9', fg='#1e40af')
        self.score_label.pack(side=tk.LEFT, padx=15)

        self.timer_label = tk.Label(score_bar, text="", font=("Segoe UI", 12, "bold"), 
                                   bg='#f1f5f9', fg='#dc2626')
        self.timer_label.pack(side=tk.RIGHT, padx=15)

        top_bar = tk.Frame(self.root, bg='#f1f5f9')
        top_bar.pack(fill=tk.X, padx=30, pady=(0, 8))

        self.theme_btn = tk.Button(top_bar, text="🌙 Dark Mode", font=("Segoe UI", 10),
                                  bg="#334155", fg="white", command=self.toggle_theme)
        self.theme_btn.pack(side=tk.RIGHT, padx=5)

        tk.Button(top_bar, text="🏆 Leaderboard", font=("Segoe UI", 10),
                 bg="#059669", fg="white", command=self.show_leaderboard).pack(side=tk.RIGHT, padx=5)

        tk.Button(top_bar, text="🎮 Quiz Mode", font=("Segoe UI", 10),
                 bg="#7c3aed", fg="white", command=self.start_quiz).pack(side=tk.RIGHT, padx=5)

        content_frame = tk.Frame(self.root, bg='#f8f9fa')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)

        self.notebook = ttk.Notebook(content_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        self.create_combination_tab()
        self.create_double_displacement_tab()
        self.create_quiz_tab()
        self.create_periodic_table_tab()
        self.create_molecular_viewer_tab()

    def on_tab_change(self, event):
        current_tab = self.notebook.index(self.notebook.select())
        if current_tab != 2:
            self.quiz_mode = False
            self.stop_timer()
            self.timer_label.config(text="")    

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def create_combination_tab(self):
        tab = tk.Frame(self.notebook, bg='#f8f9fa')
        self.notebook.add(tab, text="🔬 Combination Reactions")

        main_container = tk.Frame(tab, bg='#f8f9fa')
        main_container.pack(fill=tk.BOTH, expand=True)

        left_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))

        tk.Label(left_panel, text="🔬 Enter Reactants", font=("Segoe UI", 18, "bold"), 
                bg='#ffffff', fg='#1e40af').pack(anchor=tk.W, padx=20, pady=(20, 10))

        tk.Frame(left_panel, bg='#e0e7ff', height=2).pack(fill=tk.X, padx=20, pady=(0, 20))

        input_container = tk.Frame(left_panel, bg='#ffffff')
        input_container.pack(fill=tk.X, padx=20, pady=10)

        left_group = tk.Frame(input_container, bg='#ffffff')
        left_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(left_group, text="Reactant 1", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0,5))
        tk.Label(left_group, text="Symbol:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant1_symbol = tk.Entry(left_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.comb_reactant1_symbol.pack(fill=tk.X, pady=(0,10))
        tk.Label(left_group, text="Coefficient:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant1_coeff = tk.Entry(left_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.comb_reactant1_coeff.pack(fill=tk.X)

        tk.Label(input_container, text="➕", font=("Segoe UI", 26), bg='#ffffff', fg='#2563eb').pack(side=tk.LEFT, padx=25, pady=30)

        right_group = tk.Frame(input_container, bg='#ffffff')
        right_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(right_group, text="Reactant 2", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0,5))
        tk.Label(right_group, text="Symbol:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant2_symbol = tk.Entry(right_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.comb_reactant2_symbol.pack(fill=tk.X, pady=(0,10))
        tk.Label(right_group, text="Coefficient:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant2_coeff = tk.Entry(right_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.comb_reactant2_coeff.pack(fill=tk.X)

        button_frame = tk.Frame(left_panel, bg='#ffffff')
        button_frame.pack(fill=tk.X, padx=20, pady=25)

        tk.Button(button_frame, text="⚡ React", font=("Segoe UI", 14, "bold"), 
                bg='#2563eb', fg='white', pady=12, relief=tk.FLAT,
                command=self.perform_combination_reaction).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,8))

        tk.Button(button_frame, text="💡 Smart Hint", font=("Segoe UI", 12), 
                bg='#f59e0b', fg='white', pady=12, relief=tk.FLAT,
                command=self.show_combination_smart_hint).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,8))

        tk.Button(button_frame, text="🗑️ Clear", font=("Segoe UI", 12), 
                bg='#64748b', fg='white', pady=12, relief=tk.FLAT,
                command=self.clear_combination).pack(side=tk.LEFT, fill=tk.X, expand=True)

        right_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(15, 0))

        tk.Label(right_panel, text="📊 Reaction Result", font=("Segoe UI", 18, "bold"), 
                bg='#ffffff', fg='#1e40af').pack(anchor=tk.W, padx=20, pady=(20, 10))
        tk.Frame(right_panel, bg='#e0e7ff', height=2).pack(fill=tk.X, padx=20, pady=(0, 20))

        tk.Label(right_panel, text="Balanced Equation:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b')\
            .pack(anchor=tk.W, padx=20, pady=(0,5))

        self.comb_equation_label = tk.Label(right_panel, text="(Enter reactants and press React)", 
                                        font=("Courier New", 13, "bold"), bg='#dbeafe', fg='#0c4a6e',
                                        wraplength=380, pady=12, padx=10)
        self.comb_equation_label.pack(fill=tk.X, padx=20, pady=(0,15))

        tk.Label(right_panel, text="Correction:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b')\
            .pack(anchor=tk.W, padx=20, pady=(10,5))
        self.comb_correction_label = tk.Label(right_panel, text="", font=("Segoe UI", 10), 
                                            bg='#ffffff', fg='#059669', wraplength=380, justify=tk.LEFT)
        self.comb_correction_label.pack(anchor=tk.W, padx=20, pady=(0,15))

        tk.Label(right_panel, text="Product Color:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b')\
            .pack(anchor=tk.W, padx=20, pady=(0,5))

        color_frame = tk.Frame(right_panel, bg='#ffffff')
        color_frame.pack(anchor=tk.W, padx=20, pady=5)
        self.comb_color_canvas = Canvas(color_frame, width=110, height=65, bg='#ffffff', highlightthickness=1, highlightbackground='#cbd5e1')
        self.comb_color_canvas.pack(side=tk.LEFT, padx=(0,12))
        self.comb_product_label = tk.Label(color_frame, text="", font=("Segoe UI", 12, "bold"), bg='#ffffff')
        self.comb_product_label.pack(side=tk.LEFT)

        self.comb_status_label = tk.Label(right_panel, text="", font=("Segoe UI", 10), bg='#ffffff', 
                                        fg='#059669', wraplength=380, justify=tk.LEFT)
        self.comb_status_label.pack(anchor=tk.W, padx=20, pady=25, fill=tk.BOTH, expand=True)

    def create_double_displacement_tab(self):
        tab = tk.Frame(self.notebook, bg='#f8f9fa')
        self.notebook.add(tab, text="💥 Double Displacement")

        main_container = tk.Frame(tab, bg='#f8f9fa')
        main_container.pack(fill=tk.BOTH, expand=True)

        left_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))

        tk.Label(left_panel, text="💥 Enter Compounds", font=("Segoe UI", 18, "bold"), 
                bg='#ffffff', fg='#1e40af').pack(anchor=tk.W, padx=20, pady=(20, 10))
        tk.Frame(left_panel, bg='#e0e7ff', height=2).pack(fill=tk.X, padx=20, pady=(0, 20))

        input_container = tk.Frame(left_panel, bg='#ffffff')
        input_container.pack(fill=tk.X, padx=20, pady=10)

        left_group = tk.Frame(input_container, bg='#ffffff')
        left_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(left_group, text="Compound 1", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0,5))
        tk.Label(left_group, text="Name:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant1_symbol = tk.Entry(left_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.dd_reactant1_symbol.pack(fill=tk.X, pady=(0,10))
        tk.Label(left_group, text="Coefficient:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant1_coeff = tk.Entry(left_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.dd_reactant1_coeff.pack(fill=tk.X)

        tk.Label(input_container, text="➕", font=("Segoe UI", 26), bg='#ffffff', fg='#2563eb').pack(side=tk.LEFT, padx=25, pady=30)

        right_group = tk.Frame(input_container, bg='#ffffff')
        right_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(right_group, text="Compound 2", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0,5))
        tk.Label(right_group, text="Name:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant2_symbol = tk.Entry(right_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.dd_reactant2_symbol.pack(fill=tk.X, pady=(0,10))
        tk.Label(right_group, text="Coefficient:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant2_coeff = tk.Entry(right_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.dd_reactant2_coeff.pack(fill=tk.X)

        button_frame = tk.Frame(left_panel, bg='#ffffff')
        button_frame.pack(fill=tk.X, padx=20, pady=25)

        tk.Button(button_frame, text="⚡ React", font=("Segoe UI", 14, "bold"), 
                bg='#2563eb', fg='white', pady=12, relief=tk.FLAT,
                command=self.perform_double_displacement_reaction).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,8))

        tk.Button(button_frame, text="💡 Smart Hint", font=("Segoe UI", 12), 
                bg='#f59e0b', fg='white', pady=12, relief=tk.FLAT,
                command=self.show_dd_smart_hint).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,8))

        tk.Button(button_frame, text="🗑️ Clear", font=("Segoe UI", 12), 
                bg='#64748b', fg='white', pady=12, relief=tk.FLAT,
                command=self.clear_double_displacement).pack(side=tk.LEFT, fill=tk.X, expand=True)

        right_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(15, 0))

        tk.Label(right_panel, text="📊 Reaction Result", font=("Segoe UI", 18, "bold"), 
                bg='#ffffff', fg='#1e40af').pack(anchor=tk.W, padx=20, pady=(20, 10))
        tk.Frame(right_panel, bg='#e0e7ff', height=2).pack(fill=tk.X, padx=20, pady=(0, 20))

        tk.Label(right_panel, text="Balanced Equation:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b')\
            .pack(anchor=tk.W, padx=20, pady=(0,5))

        self.dd_equation_label = tk.Label(right_panel, text="(Enter compounds and press React)", 
                                        font=("Courier New", 13, "bold"), bg='#dbeafe', fg='#0c4a6e',
                                        wraplength=380, pady=12, padx=10)
        self.dd_equation_label.pack(fill=tk.X, padx=20, pady=(0,15))

        tk.Label(right_panel, text="Precipitate Formed:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b')\
            .pack(anchor=tk.W, padx=20, pady=(10,5))
        self.dd_precipitate_label = tk.Label(right_panel, text="", font=("Segoe UI", 11), 
                                            fg='#dc2626', bg='#ffffff', wraplength=380, justify=tk.LEFT)
        self.dd_precipitate_label.pack(anchor=tk.W, padx=20, pady=(0,15))

        tk.Label(right_panel, text="Precipitate Color:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b')\
            .pack(anchor=tk.W, padx=20, pady=(0,5))

        color_frame = tk.Frame(right_panel, bg='#ffffff')
        color_frame.pack(anchor=tk.W, padx=20, pady=5)
        self.dd_color_canvas = Canvas(color_frame, width=110, height=65, bg='#ffffff', highlightthickness=1, highlightbackground='#cbd5e1')
        self.dd_color_canvas.pack(side=tk.LEFT, padx=(0,12))
        self.dd_color_label = tk.Label(color_frame, text="", font=("Segoe UI", 12, "bold"), bg='#ffffff')
        self.dd_color_label.pack(side=tk.LEFT)

        self.dd_status_label = tk.Label(right_panel, text="", font=("Segoe UI", 10), bg='#ffffff', 
                                    fg='#059669', wraplength=380, justify=tk.LEFT)
        self.dd_status_label.pack(anchor=tk.W, padx=20, pady=25, fill=tk.BOTH, expand=True)

    def create_quiz_tab(self):
        tab = tk.Frame(self.notebook, bg='#f8f9fa')
        self.notebook.add(tab, text="🎮 Quiz Mode")

        self.quiz_frame = tk.Frame(tab, bg='#f8f9fa')
        self.quiz_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        welcome_frame = tk.Frame(self.quiz_frame, bg='#ffffff', relief=tk.RAISED, bd=1)
        welcome_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(welcome_frame, text="🎮 Quiz Mode", font=("Segoe UI", 24, "bold"), 
                bg='#ffffff', fg='#7c3aed').pack(pady=20)

        tk.Label(welcome_frame, text="Challenge yourself with random chemical reactions!",
                font=("Segoe UI", 14), bg='#ffffff', fg='#475569').pack(pady=10)

        tk.Label(welcome_frame, text="• Answer questions within 30 seconds total\n• Get bonus points for correct answers\n• Track your high scores",
                font=("Segoe UI", 12), bg='#ffffff', fg='#64748b', justify=tk.LEFT).pack(pady=20, padx=20)

        tk.Button(welcome_frame, text="🚀 Start Quiz", font=("Segoe UI", 16, "bold"),
                bg='#7c3aed', fg='white', padx=30, pady=15, relief=tk.FLAT,
                command=self.start_quiz).pack(pady=30)

    def create_periodic_table_tab(self):
        tab = tk.Frame(self.notebook, bg='#f8f9fa')
        self.notebook.add(tab, text="🧪 Periodic Table")

        tk.Label(tab, text="🧪 Interactive Periodic Table", font=("Segoe UI", 20, "bold"),
                bg='#f8f9fa', fg='#1e40af').pack(pady=10)

        self.pt_info_frame = tk.Frame(tab, bg='#ffffff', relief=tk.RAISED, bd=1, height=120)
        self.pt_info_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        self.pt_info_frame.pack_propagate(False)

        self.pt_info_label = tk.Label(self.pt_info_frame, 
            text="👆 Click on any element to see its details\n\n"
                 "🎨 Color Legend:\n"
                 "🔴 Alkali Metal | 🟠 Alkaline Earth | 🟡 Halogen | 🟢 Nonmetal\n"
                 "🔵 Transition Metal | 🟣 Metalloid | ⚪ Noble Gas | ⚫ Post-transition",
            font=("Segoe UI", 11), bg='#ffffff', fg='#475569', justify=tk.LEFT)
        self.pt_info_label.pack(padx=20, pady=10, anchor=tk.W)

        canvas_frame = tk.Frame(tab, bg='#f8f9fa')
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        pt_canvas = Canvas(canvas_frame, bg='#f8f9fa', highlightthickness=0)
        scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=pt_canvas.yview)
        pt_canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        pt_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        pt_inner = tk.Frame(pt_canvas, bg='#f8f9fa')
        pt_canvas.create_window((0, 0), window=pt_inner, anchor=tk.NW)

        element_positions = {
            'H': (1, 1), 'He': (18, 1),
            'Li': (1, 2), 'Be': (2, 2), 'B': (13, 2), 'C': (14, 2), 'N': (15, 2), 'O': (16, 2), 'F': (17, 2), 'Ne': (18, 2),
            'Na': (1, 3), 'Mg': (2, 3), 'Al': (13, 3), 'Si': (14, 3), 'P': (15, 3), 'S': (16, 3), 'Cl': (17, 3), 'Ar': (18, 3),
            'K': (1, 4), 'Ca': (2, 4), 'Fe': (8, 4), 'Cu': (11, 4), 'Zn': (12, 4),
            'Ag': (11, 5), 'Au': (11, 6), 'Hg': (12, 6), 'Pb': (14, 6),
        }

        for symbol, data in self.periodic_table.items():
            pos = element_positions.get(symbol, (1, 1))
            col, row = pos

            elem_frame = tk.Frame(pt_inner, bg=data['color'], width=60, height=70, 
                                  relief=tk.RAISED, bd=2, cursor='hand2')
            elem_frame.grid(row=row, column=col, padx=3, pady=3, sticky='nsew')
            elem_frame.grid_propagate(False)

            tk.Label(elem_frame, text=str(data['number']), font=("Segoe UI", 8), 
                    bg=data['color'], fg='#1f2937').pack(anchor=tk.NW, padx=3, pady=1)
            tk.Label(elem_frame, text=symbol, font=("Segoe UI", 14, "bold"), 
                    bg=data['color'], fg='#1f2937').pack(expand=True)
            tk.Label(elem_frame, text=data['name'][:8], font=("Segoe UI", 7), 
                    bg=data['color'], fg='#1f2937').pack(pady=(0, 2))

            elem_frame.bind('<Button-1>', lambda e, s=symbol, d=data: self.show_element_details(s, d))
            for child in elem_frame.winfo_children():
                child.bind('<Button-1>', lambda e, s=symbol, d=data: self.show_element_details(s, d))

        for i in range(1, 19):
            pt_inner.grid_columnconfigure(i, weight=1, minsize=60)
        for i in range(1, 8):
            pt_inner.grid_rowconfigure(i, weight=1, minsize=70)

        pt_inner.update_idletasks()
        pt_canvas.config(scrollregion=pt_canvas.bbox('all'))

    def show_element_details(self, symbol, data):
        info_text = (
            f"🔬 {data['name']} ({symbol})\n"
            f"📊 Atomic Number: {data['number']}\n"
            f"⚖️ Atomic Mass: {data['mass']} u\n"
            f"📍 Group: {data['group']} | Period: {data['period']}\n"
            f"🏷️ Category: {data['category']}"
        )
        self.pt_info_label.config(text=info_text, font=("Segoe UI", 13, "bold"), fg='#1e40af')

    def create_molecular_viewer_tab(self):
        tab = tk.Frame(self.notebook, bg='#f8f9fa')
        self.notebook.add(tab, text="🧬 Molecular Viewer")

        tk.Label(tab, text="🧬 3D Molecular Viewer", font=("Segoe UI", 20, "bold"),
                bg='#f8f9fa', fg='#1e40af').pack(pady=10)

        input_frame = tk.Frame(tab, bg='#ffffff', relief=tk.RAISED, bd=1)
        input_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(input_frame, text="Enter Compound Formula:", font=("Segoe UI", 12, "bold"),
                bg='#ffffff', fg='#1e293b').pack(side=tk.LEFT, padx=15, pady=10)

        self.mv_formula_entry = tk.Entry(input_frame, font=("Segoe UI", 12), bg='#f1f5f9', 
                                         relief=tk.FLAT, width=20)
        self.mv_formula_entry.pack(side=tk.LEFT, padx=5, pady=10)
        self.mv_formula_entry.insert(0, "H2O")

        tk.Button(input_frame, text="🔍 Visualize", font=("Segoe UI", 11, "bold"),
                 bg='#2563eb', fg='white', padx=15, pady=5, relief=tk.FLAT,
                 command=self.visualize_molecule).pack(side=tk.LEFT, padx=10, pady=10)

        presets_frame = tk.Frame(tab, bg='#f8f9fa')
        presets_frame.pack(fill=tk.X, padx=20, pady=(0, 10))

        presets = ["H2O", "CO2", "NH3", "CH4", "NaCl", "C6H12O6"]
        for preset in presets:
            tk.Button(presets_frame, text=preset, font=("Segoe UI", 10),
                     bg='#e0e7ff', fg='#1e40af', padx=10, pady=3, relief=tk.FLAT,
                     command=lambda p=preset: self.load_preset_molecule(p)).pack(side=tk.LEFT, padx=3)

        canvas_frame = tk.Frame(tab, bg='#ffffff', relief=tk.RAISED, bd=1)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.mv_canvas = Canvas(canvas_frame, bg='#0f172a', highlightthickness=0)
        self.mv_canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.mv_info_label = tk.Label(tab, text="Enter a formula and click Visualize to see the molecular structure",
                                     font=("Segoe UI", 11), bg='#f8f9fa', fg='#64748b')
        self.mv_info_label.pack(pady=5)

        self.visualize_molecule()

    def load_preset_molecule(self, formula):
        self.mv_formula_entry.delete(0, tk.END)
        self.mv_formula_entry.insert(0, formula)
        self.visualize_molecule()

    def visualize_molecule(self):
        formula = self.mv_formula_entry.get().strip()
        self.mv_canvas.delete("all")

        width = self.mv_canvas.winfo_width()
        height = self.mv_canvas.winfo_height()
        if width < 100:
            width, height = 800, 500

        cx, cy = width // 2, height // 2

        atoms = self.parse_formula(formula)

        if not atoms:
            self.mv_canvas.create_text(cx, cy, text="Invalid Formula", 
                                      font=("Segoe UI", 20, "bold"), fill='#dc2626')
            return

        total_atoms = sum(atoms.values())

        if total_atoms == 1:
            symbol = list(atoms.keys())[0]
            self.draw_atom(cx, cy, 50, symbol, atoms[symbol])

        elif total_atoms == 2:
            symbols = list(atoms.keys())
            self.draw_atom(cx - 80, cy, 45, symbols[0], atoms[symbols[0]])
            self.draw_atom(cx + 80, cy, 45, symbols[1], atoms[symbols[1]])
            self.mv_canvas.create_line(cx - 35, cy, cx + 35, cy, fill='#94a3b8', width=8)

        elif formula == "H2O":
            self.draw_atom(cx, cy - 60, 40, "O", 1)
            self.draw_atom(cx - 70, cy + 50, 30, "H", 2)
            self.draw_atom(cx + 70, cy + 50, 30, "H", 2)
            self.mv_canvas.create_line(cx - 10, cy - 30, cx - 50, cy + 25, fill='#94a3b8', width=6)
            self.mv_canvas.create_line(cx + 10, cy - 30, cx + 50, cy + 25, fill='#94a3b8', width=6)

        elif formula == "CO2":
            self.draw_atom(cx - 100, cy, 35, "O", 2)
            self.draw_atom(cx, cy, 45, "C", 1)
            self.draw_atom(cx + 100, cy, 35, "O", 2)
            self.mv_canvas.create_line(cx - 65, cy - 5, cx - 30, cy - 5, fill='#94a3b8', width=4)
            self.mv_canvas.create_line(cx - 65, cy + 5, cx - 30, cy + 5, fill='#94a3b8', width=4)
            self.mv_canvas.create_line(cx + 30, cy - 5, cx + 65, cy - 5, fill='#94a3b8', width=4)
            self.mv_canvas.create_line(cx + 30, cy + 5, cx + 65, cy + 5, fill='#94a3b8', width=4)

        elif formula == "NH3":
            self.draw_atom(cx, cy - 50, 42, "N", 1)
            self.draw_atom(cx - 70, cy + 40, 28, "H", 3)
            self.draw_atom(cx + 70, cy + 40, 28, "H", 3)
            self.draw_atom(cx, cy + 70, 28, "H", 3)
            self.mv_canvas.create_line(cx - 15, cy - 20, cx - 50, cy + 20, fill='#94a3b8', width=5)
            self.mv_canvas.create_line(cx + 15, cy - 20, cx + 50, cy + 20, fill='#94a3b8', width=5)
            self.mv_canvas.create_line(cx, cy - 10, cx, cy + 40, fill='#94a3b8', width=5)

        elif formula == "CH4":
            self.draw_atom(cx, cy, 45, "C", 1)
            self.draw_atom(cx, cy - 90, 28, "H", 4)
            self.draw_atom(cx - 80, cy + 30, 28, "H", 4)
            self.draw_atom(cx + 80, cy + 30, 28, "H", 4)
            self.draw_atom(cx, cy + 70, 28, "H", 4)
            for angle in [90, 210, 330, 270]:
                rad = math.radians(angle)
                x1 = cx + 30 * math.cos(rad)
                y1 = cy + 30 * math.sin(rad)
                x2 = cx + 75 * math.cos(rad)
                y2 = cy + 75 * math.sin(rad)
                self.mv_canvas.create_line(x1, y1, x2, y2, fill='#94a3b8', width=5)

        elif formula == "C6H12O6":
            self.draw_glucose_ring(cx, cy)

        else:
            self.draw_generic_molecule(cx, cy, atoms)

        atom_list = ", ".join([f"{k}({v})" for k, v in atoms.items()])
        self.mv_info_label.config(
            text=f"Formula: {formula} | Atoms: {atom_list} | Total: {total_atoms} atoms",
            font=("Segoe UI", 12, "bold"), fg='#1e40af'
        )

    def parse_formula(self, formula):
        pattern = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(pattern, formula)
        atoms = {}
        for element, count in matches:
            atoms[element] = atoms.get(element, 0) + (int(count) if count else 1)
        return atoms

    def draw_atom(self, x, y, radius, symbol, count):
        color = self.periodic_table.get(symbol, {}).get('color', '#94a3b8')

        self.mv_canvas.create_oval(x - radius + 3, y - radius + 3, 
                                   x + radius + 3, y + radius + 3, 
                                   fill='#000000', outline='', stipple='gray50')

        self.mv_canvas.create_oval(x - radius, y - radius, 
                                   x + radius, y + radius, 
                                   fill=color, outline='#ffffff', width=3)

        self.mv_canvas.create_text(x, y, text=symbol, 
                                   font=("Segoe UI", max(12, radius // 2), "bold"), 
                                   fill='#1f2937')

        if count > 1:
            self.mv_canvas.create_text(x + radius - 8, y - radius + 12, 
                                       text=str(count), 
                                       font=("Segoe UI", 10, "bold"), 
                                       fill='#dc2626')

    def draw_glucose_ring(self, cx, cy):
        radius = 80
        points = []
        for i in range(6):
            angle = math.radians(60 * i - 90)
            px = cx + radius * math.cos(angle)
            py = cy + radius * math.sin(angle)
            points.append((px, py))

            if i == 0:
                self.draw_atom(px, py, 30, "O", 1)
            else:
                self.draw_atom(px, py, 28, "C", 1)

        for i in range(6):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % 6]
            self.mv_canvas.create_line(x1, y1, x2, y2, fill='#94a3b8', width=5)

        oh_positions = [
            (cx - 120, cy - 60), (cx - 120, cy + 60),
            (cx, cy + 120), (cx + 120, cy + 60),
            (cx + 120, cy - 60)
        ]
        for ox, oy in oh_positions:
            self.draw_atom(ox, oy, 22, "O", 1)
            self.draw_atom(ox + 30, oy, 18, "H", 1)
            self.mv_canvas.create_line(ox - 15, oy, ox - 5, oy, fill='#94a3b8', width=3)
            self.mv_canvas.create_line(ox + 15, oy, ox + 20, oy, fill='#94a3b8', width=3)

    def draw_generic_molecule(self, cx, cy, atoms):
        total = sum(atoms.values())
        angle_step = 360 / max(total, 1)
        radius = 100

        idx = 0
        for symbol, count in atoms.items():
            for _ in range(count):
                angle = math.radians(angle_step * idx)
                px = cx + radius * math.cos(angle)
                py = cy + radius * math.sin(angle)
                self.draw_atom(px, py, 30, symbol, 1)

                self.mv_canvas.create_line(cx + 20 * math.cos(angle), cy + 20 * math.sin(angle),
                                          px - 25 * math.cos(angle), py - 25 * math.sin(angle),
                                          fill='#94a3b8', width=4)
                idx += 1

        self.mv_canvas.create_oval(cx - 15, cy - 15, cx + 15, cy + 15, 
                                   fill='#475569', outline='#ffffff', width=2)

    def show_combination_smart_hint(self):
        r1 = self.comb_reactant1_symbol.get().strip()
        r2 = self.comb_reactant2_symbol.get().strip()

        if not r1 and not r2:
            messagebox.showwarning("Hint", "Please enter at least one reactant first!")
            return

        hint_text = "💡 Smart Hint:\n\n"

        for reactant in [r1, r2]:
            if not reactant:
                continue

            symbol = self.extract_element_symbol(reactant)
            self.cursor.execute("SELECT * FROM Elements WHERE symbol = ? OR LOWER(name) = LOWER(?)", 
                               (symbol, reactant))
            elem = self.cursor.fetchone()

            if elem:
                hint_text += (
                    f"🔬 {elem[1]} ({elem[0]})\n"
                    f"   • Atomic Number: {elem[2]}\n"
                    f"   • Atomic Mass: {elem[3]} u\n"
                    f"   • Group {elem[4]}, Period {elem[5]}\n"
                    f"   • Type: {elem[6]}\n\n"
                )
            else:
                self.cursor.execute("""
                    SELECT cc.element_symbol, cc.count, e.name, e.category 
                    FROM Compound_Composition cc
                    LEFT JOIN Elements e ON cc.element_symbol = e.symbol
                    WHERE cc.compound_name = ?
                """, (reactant,))
                comp = self.cursor.fetchall()
                if comp:
                    hint_text += f"🧪 Compound: {reactant}\n   Composition:\n"
                    for elem_sym, count, name, cat in comp:
                        hint_text += f"   • {name or elem_sym}: {count} atom(s)\n"
                    hint_text += "\n"
                else:
                    hint_text += f"❓ {reactant}: Not found in database\n\n"

        if r1 and r2:
            hint_text += "⚡ Reaction Tip:\n"
            hint_text += "   Check if the reactants form a known compound!\n"
            hint_text += "   Remember: Coefficients must be in the simplest whole number ratio."

        messagebox.showinfo("💡 Smart Hint", hint_text)

    def show_dd_smart_hint(self):
        r1 = self.dd_reactant1_symbol.get().strip()
        r2 = self.dd_reactant2_symbol.get().strip()

        if not r1 and not r2:
            messagebox.showwarning("Hint", "Please enter at least one compound first!")
            return

        hint_text = "💡 Smart Hint - Double Displacement:\n\n"

        for compound in [r1, r2]:
            if not compound:
                continue

            self.cursor.execute("""
                SELECT cc.element_symbol, cc.count, e.name, e.category 
                FROM Compound_Composition cc
                LEFT JOIN Elements e ON cc.element_symbol = e.symbol
                WHERE cc.compound_name = ?
            """, (compound,))
            comp = self.cursor.fetchall()

            if comp:
                hint_text += f"🧪 {compound}:\n"
                for elem_sym, count, name, cat in comp:
                    hint_text += f"   • {name or elem_sym} ({elem_sym}): {count} atom(s)\n"
                hint_text += "\n"
            else:
                symbol = self.extract_element_symbol(compound)
                self.cursor.execute("SELECT * FROM Elements WHERE symbol = ?", (symbol,))
                elem = self.cursor.fetchone()
                if elem:
                    hint_text += (
                        f"🔬 {elem[1]} ({elem[0]}) - {elem[6]}\n"
                        f"   Group {elem[4]}, Period {elem[5]}\n\n"
                    )
                else:
                    hint_text += f"❓ {compound}: Not found in database\n\n"

        if r1 and r2:
            hint_text += "⚡ Reaction Tip:\n"
            hint_text += "   In double displacement, ions swap partners!\n"
            hint_text += "   Look for precipitate formation (insoluble product)."

        messagebox.showinfo("💡 Smart Hint", hint_text)

    def extract_element_symbol(self, text):
        match = re.match(r'([A-Z][a-z]?)', text)
        return match.group(1) if match else text

    def start_quiz(self):
        self.cursor.execute("""
            SELECT r.id, r.equation, p.name, r.reaction_type 
            FROM Reactions r 
            JOIN Products p ON r.product_id = p.id 
            ORDER BY RANDOM() LIMIT 10
        """)

        self.quiz_questions = self.cursor.fetchall()
        if not self.quiz_questions:
            messagebox.showerror("Error", "No questions available")
            return

        self.current_question = 0
        self.quiz_score = 0
        self.hints_used = 0

        self.quiz_mode = True
        self.notebook.select(2)

        self.time_remaining = 30
        self.timer_label.config(text=f"⏱️ Time: {self.time_remaining}s", fg='#059669')
        self.start_quiz_timer()

        self.show_quiz_question()

    def start_quiz_timer(self):
        self.update_quiz_timer()

    def show_quiz_question(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        if self.current_question >= len(self.quiz_questions):
            self.end_quiz("completed")
            return

        reaction_id, equation, product_name, reaction_type = self.quiz_questions[self.current_question]

        q_frame = tk.Frame(self.quiz_frame, bg='#ffffff', relief=tk.RAISED, bd=1)
        q_frame.pack(fill=tk.BOTH, expand=True)

        progress_text = f"Question {self.current_question + 1}/{len(self.quiz_questions)}"
        tk.Label(q_frame, text=progress_text, font=("Segoe UI", 12, "bold"), 
                bg='#ffffff', fg='#7c3aed').pack(anchor=tk.W, padx=20, pady=(20, 10))

        tk.Label(q_frame, text="Balance this equation:", font=("Segoe UI", 14, "bold"),
                bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(15, 10))

        left_side = equation.split('→')[0]
        reactants = left_side.split('+')

        r1 = re.sub(r'^\d+', '', reactants[0].strip())
        r2 = re.sub(r'^\d+', '', reactants[1].strip())

        tk.Label(q_frame, text=f"___ {r1} + ___ {r2} → ... {product_name}",
        font=("Courier New", 14, "bold"), bg='#dbeafe', fg='#0c4a6e',
        padx=20, pady=15).pack(fill=tk.X, padx=20, pady=(10, 20))

        input_frame = tk.Frame(q_frame, bg='#ffffff')
        input_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(input_frame, text="Coefficient 1:", font=("Segoe UI", 11), bg='#ffffff').pack(side=tk.LEFT, padx=5)
        self.quiz_coeff1 = tk.Entry(input_frame, font=("Segoe UI", 12), bg='#f1f5f9', width=5, relief=tk.FLAT)
        self.quiz_coeff1.pack(side=tk.LEFT, padx=5)

        tk.Label(input_frame, text="Coefficient 2:", font=("Segoe UI", 11), bg='#ffffff').pack(side=tk.LEFT, padx=5)
        self.quiz_coeff2 = tk.Entry(input_frame, font=("Segoe UI", 12), bg='#f1f5f9', width=5, relief=tk.FLAT)
        self.quiz_coeff2.pack(side=tk.LEFT, padx=5)

        btn_frame = tk.Frame(q_frame, bg='#ffffff')
        btn_frame.pack(fill=tk.X, padx=20, pady=20)

        tk.Button(btn_frame, text="✓ Submit", font=("Segoe UI", 12, "bold"),
                bg='#059669', fg='white', pady=10, relief=tk.FLAT,
                command=lambda: self.check_quiz_answer(reaction_id, product_name)).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        tk.Button(btn_frame, text="⏭️ Skip", font=("Segoe UI", 12),
                bg='#64748b', fg='white', pady=10, relief=tk.FLAT,
                command=self.skip_quiz_question).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.quiz_coeff1.focus()

    def update_quiz_timer(self):
        if not self.quiz_mode:
            return

        if self.time_remaining <= 0:
            self.stop_timer()
            self.timer_label.config(text="")
            messagebox.showinfo("⏱️ Time Up!", "Time is over! Quiz ended.")
            self.end_quiz("timeout")
            return

        self.time_remaining -= 1
        color = '#dc2626' if self.time_remaining < 10 else '#059669'
        self.timer_label.config(text=f"⏱️ Time: {self.time_remaining}s", fg=color)

        self.timer_id = self.root.after(1000, self.update_quiz_timer)

    def check_quiz_answer(self, reaction_id, product_name):
        if not self.quiz_mode:
            return

        try:
            user_c1 = int(self.quiz_coeff1.get().strip() or 0)
            user_c2 = int(self.quiz_coeff2.get().strip() or 0)

            if user_c1 == 0 or user_c2 == 0:
                messagebox.showwarning("Error", "Please enter valid coefficients")
                return

            self.cursor.execute("""
                SELECT rx.name, rr.coefficient FROM Reaction_Reactants rr
                JOIN Reactants rx ON rr.reactant_id = rx.id
                WHERE rr.reaction_id = ? LIMIT 2
            """, (reaction_id,))

            coeffs = self.cursor.fetchall()
            correct_c1, correct_c2 = coeffs[0][1], coeffs[1][1]

            # FIX: Check proportional coefficients
            if self.are_coefficients_proportional(user_c1, user_c2, correct_c1, correct_c2):
                points = 10 + max(0, self.time_remaining // 6)
                self.quiz_score += points
                messagebox.showinfo("✓ Correct!", f"Well done! +{points} points")
            else:
                messagebox.showinfo("✗ Incorrect", f"Correct ratio: {correct_c1}:{correct_c2}")

            self.current_question += 1
            self.show_quiz_question()

        except ValueError:
            messagebox.showerror("Error", "Please enter numbers only")

    def are_coefficients_proportional(self, u1, u2, c1, c2):
        """Check if user coefficients are proportional to correct coefficients"""
        if c1 == 0 or c2 == 0:
            return u1 == c1 and u2 == c2
        return (u1 * c2) == (u2 * c1)

    def skip_quiz_question(self):
        if not self.quiz_mode:
            return
        self.current_question += 1
        self.show_quiz_question()

    def end_quiz(self, reason):
        self.stop_timer()
        self.timer_label.config(text="")
        self.quiz_mode = False

        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        result_frame = tk.Frame(self.quiz_frame, bg='#ffffff', relief=tk.RAISED, bd=1)
        result_frame.pack(fill=tk.BOTH, expand=True)

        if reason == "timeout":
            title_text = "⏱️ Time's Up!"
            title_color = '#dc2626'
        else:
            title_text = "🎉 Quiz Completed!"
            title_color = '#059669'

        tk.Label(result_frame, text=title_text, font=("Segoe UI", 24, "bold"),
                bg='#ffffff', fg=title_color).pack(pady=20)

        max_score = len(self.quiz_questions) * 15
        accuracy = (self.quiz_score / max_score * 100) if max_score > 0 else 0

        tk.Label(result_frame, text=f"Questions Answered: {self.current_question}/{len(self.quiz_questions)}\nFinal Score: {self.quiz_score}\nAccuracy: {accuracy:.1f}%",
                font=("Segoe UI", 18), bg='#ffffff', fg='#1e40af').pack(pady=20)

        player_name = simpledialog.askstring("Save Score", "Enter your name:")
        if player_name:
            self.cursor.execute("""
                INSERT INTO Scores (player_name, score, accuracy)
                VALUES (?, ?, ?)
            """, (player_name, self.quiz_score, accuracy))
            self.conn.commit()
            messagebox.showinfo("Success", f"Score saved for {player_name}!")

        tk.Button(result_frame, text="🎮 Take Quiz Again", font=("Segoe UI", 14, "bold"),
                bg='#7c3aed', fg='white', padx=20, pady=15, relief=tk.FLAT,
                command=self.start_quiz).pack(pady=20)

        tk.Button(result_frame, text="🏆 View Leaderboard", font=("Segoe UI", 14, "bold"),
                bg='#059669', fg='white', padx=20, pady=15, relief=tk.FLAT,
                command=self.show_leaderboard).pack(pady=10)

    def show_leaderboard(self):
        lb_window = tk.Toplevel(self.root)
        lb_window.title("🏆 Leaderboard")
        lb_window.geometry("500x400")
        lb_window.configure(bg='#f8f9fa')

        tk.Label(lb_window, text="🏆 High Scores", font=("Segoe UI", 20, "bold"),
                bg='#f8f9fa', fg='#059669').pack(pady=15)

        self.cursor.execute("""
            SELECT player_name, score, accuracy FROM Scores
            ORDER BY score DESC LIMIT 10
        """)

        scores = self.cursor.fetchall()

        if not scores:
            tk.Label(lb_window, text="No scores yet. Start a quiz!",
                    font=("Segoe UI", 12), bg='#f8f9fa', fg='#64748b').pack(pady=20)
        else:
            for i, (name, score, accuracy) in enumerate(scores, 1):
                medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"#{i}"
                tk.Label(lb_window, text=f"{medal} {name} - Score: {score}",
                        font=("Segoe UI", 12), bg='#f8f9fa', fg='#1e293b').pack(pady=5)

    def clear_combination(self):
        self.comb_reactant1_symbol.delete(0, tk.END)
        self.comb_reactant2_symbol.delete(0, tk.END)
        self.comb_reactant1_coeff.delete(0, tk.END)
        self.comb_reactant2_coeff.delete(0, tk.END)
        self.comb_equation_label.config(text="(Enter reactants and press React)")
        self.comb_correction_label.config(text="")
        self.comb_status_label.config(text="")
        self.comb_product_label.config(text="")
        self.comb_color_canvas.delete("all")

    def clear_double_displacement(self):
        self.dd_reactant1_symbol.delete(0, tk.END)
        self.dd_reactant2_symbol.delete(0, tk.END)
        self.dd_reactant1_coeff.delete(0, tk.END)
        self.dd_reactant2_coeff.delete(0, tk.END)
        self.dd_equation_label.config(text="(Enter compounds and press React)")
        self.dd_precipitate_label.config(text="")
        self.dd_status_label.config(text="")
        self.dd_color_label.config(text="")
        self.dd_color_canvas.delete("all")

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        if self.is_dark:
            bg_color, fg_color, frame_bg, entry_bg = '#1f2937', '#e2e8f0', '#334155', '#475569'
            self.theme_btn.config(text="☀️ Light Mode", bg="#64748b")
        else:
            bg_color, fg_color, frame_bg, entry_bg = '#f8f9fa', '#1e293b', '#ffffff', '#f1f5f9'
            self.theme_btn.config(text="🌙 Dark Mode", bg="#334155")

        self.root.configure(bg=bg_color)
        for widget in self.root.winfo_children():
            self.recursive_theme_change(widget, bg_color, fg_color, frame_bg, frame_bg, entry_bg)

    def recursive_theme_change(self, widget, bg, fg, frame_bg, label_bg, entry_bg):
        try:
            widget_type = widget.winfo_class()
            if widget_type in ('Frame', 'TFrame'):
                widget.configure(bg=frame_bg)
            elif widget_type in ('Label', 'TLabel'):
                widget.configure(bg=label_bg, fg=fg)
            elif widget_type in ('Entry', 'TEntry'):
                widget.configure(bg=entry_bg, fg=fg)
            elif widget_type == 'Canvas':
                widget.configure(bg=frame_bg)
            for child in widget.winfo_children():
                self.recursive_theme_change(child, bg, fg, frame_bg, label_bg, entry_bg)
        except: pass

    def update_score(self):
        accuracy = (self.score / self.total_attempts * 100) if self.total_attempts > 0 else 0
        self.score_label.config(text=f"Score: {self.score} | Accuracy: {accuracy:.1f}%")

    def get_compound_composition(self, compound_name):
        self.cursor.execute("SELECT element_symbol, count FROM Compound_Composition WHERE compound_name = ?", (compound_name,))
        result = self.cursor.fetchall()
        return {elem: cnt for elem, cnt in result} if result else None

    def balance_equation(self, r1, r2, prod):
        r1_comp = self.get_compound_composition(r1) or {r1: 1}
        r2_comp = self.get_compound_composition(r2) or {r2: 1}
        prod_comp = self.get_compound_composition(prod) or {prod: 1}
        for c1 in range(1, 11):
            for c2 in range(1, 11):
                for cp in range(1, 11):
                    left = {}
                    for e, c in r1_comp.items(): left[e] = left.get(e, 0) + c * c1
                    for e, c in r2_comp.items(): left[e] = left.get(e, 0) + c * c2
                    right = {e: c * cp for e, c in prod_comp.items()}
                    if left == right: return c1, c2, cp
        return None

    def display_color(self, color_name, canvas, label):
        canvas.delete("all")
        color_map = {'White': '#ffffff', 'Colorless': '#e0e7ff', 'Red-Brown': '#b91c1c', 'Reddish-Brown': '#d2691e', 'Gray-White': '#d1d5db', 'Yellow': '#fbbf24'}
        hex_color = color_map.get(color_name, '#cbd5e1')
        canvas.create_rectangle(3, 3, 107, 62, fill=hex_color, outline='#94a3b8', width=2)
        canvas.create_text(55, 32, text=color_name, font=("Segoe UI", 9, "bold"), fill='#1f2937' if color_name not in ['White', 'Colorless'] else '#1e40af')
        label.config(text=color_name)

    def perform_combination_reaction(self):
        try:
            r1 = self.comb_reactant1_symbol.get().strip().lower()
            r2 = self.comb_reactant2_symbol.get().strip().lower()
            user_c1 = int(self.comb_reactant1_coeff.get().strip() or 1)
            user_c2 = int(self.comb_reactant2_coeff.get().strip() or 1)
            if not r1 or not r2:
                messagebox.showwarning("Input Error", "Please enter both reactants")
                return
            self.total_attempts += 1
            self.cursor.execute("""
                SELECT r.equation, p.name, p.color FROM Reactions r
                JOIN Products p ON r.product_id = p.id
                WHERE r.reaction_type = 'Combination'
                AND r.id IN (SELECT reaction_id FROM Reaction_Reactants WHERE reactant_id = (SELECT id FROM Reactants WHERE LOWER(name) = ?))
                AND r.id IN (SELECT reaction_id FROM Reaction_Reactants WHERE reactant_id = (SELECT id FROM Reactants WHERE LOWER(name) = ?))
                LIMIT 1
            """, (r1, r2))
            result = self.cursor.fetchone()
            if result:
                equation, prod_name, color = result
                self.cursor.execute("SELECT name FROM Reactants WHERE LOWER(name) = ?", (r1,))
                orig_r1 = self.cursor.fetchone()[0]
                self.cursor.execute("SELECT name FROM Reactants WHERE LOWER(name) = ?", (r2,))
                orig_r2 = self.cursor.fetchone()[0]
                balanced = self.balance_equation(orig_r1, orig_r2, prod_name)
                if balanced:
                    c1, c2, cp = balanced
                    self.comb_equation_label.config(text=f"{c1}{orig_r1} + {c2}{orig_r2} → {cp}{prod_name}")
                    self.display_color(color, self.comb_color_canvas, self.comb_product_label)
                    if self.are_coefficients_proportional(user_c1, user_c2, c1, c2):
                        self.score += 1
                        self.comb_status_label.config(text="🎉 Excellent! Correct balancing.", fg='#059669')
                    else:
                        self.comb_status_label.config(text=f"⚠ Auto-balanced: {c1} & {c2} were needed.", fg='#d97706')
            else:
                self.comb_equation_label.config(text="No reaction found", fg='#dc2626')
            self.update_score()
        except ValueError: messagebox.showerror("Error", "Coefficients must be numbers")

    def perform_double_displacement_reaction(self):
        try:
            r1 = self.dd_reactant1_symbol.get().strip()
            r2 = self.dd_reactant2_symbol.get().strip()
            user_c1 = int(self.dd_reactant1_coeff.get().strip() or 1)
            user_c2 = int(self.dd_reactant2_coeff.get().strip() or 1)
            if not r1 or not r2:
                messagebox.showwarning("Input Error", "Please enter both compounds")
                return
            self.total_attempts += 1
            r1_l, r2_l = r1.lower(), r2.lower()
            self.cursor.execute("""
                SELECT r.id, r.equation, p.name, p.color FROM Reactions r
                JOIN Products p ON r.product_id = p.id
                WHERE r.reaction_type = 'Double Displacement'
                AND EXISTS (SELECT 1 FROM Reaction_Reactants rr JOIN Reactants rx ON rr.reactant_id = rx.id WHERE rr.reaction_id = r.id AND LOWER(rx.name) = ?)
                AND EXISTS (SELECT 1 FROM Reaction_Reactants rr JOIN Reactants rx ON rr.reactant_id = rx.id WHERE rr.reaction_id = r.id AND LOWER(rx.name) = ?)
                LIMIT 1
            """, (r1_l, r2_l))
            result = self.cursor.fetchone()
            if result:
                rid, eq, prod_name, color = result
                self.cursor.execute("SELECT rx.name, rr.coefficient FROM Reaction_Reactants rr JOIN Reactants rx ON rr.reactant_id = rx.id WHERE rr.reaction_id = ?", (rid,))
                correct_coeffs = {name.lower(): coeff for name, coeff in self.cursor.fetchall()}
                c1, c2 = correct_coeffs.get(r1_l, 1), correct_coeffs.get(r2_l, 1)
                self.dd_equation_label.config(text=eq, fg='#0c4a6e')
                self.dd_precipitate_label.config(text=f"↓ {prod_name} (Precipitate)")
                self.display_color(color, self.dd_color_canvas, self.dd_color_label)
                if self.are_coefficients_proportional(user_c1, user_c2, c1, c2):
                    self.score += 1
                    self.dd_status_label.config(text="🎉 Perfect balancing!", fg='#059669')
                else:
                    self.dd_status_label.config(text=f"⚠ Correction: {c1} & {c2} were required.", fg='#d97706')
            else:
                self.dd_equation_label.config(text="No reaction occurs", fg='#dc2626')
            self.update_score()
        except ValueError: messagebox.showerror("Error", "Coefficients must be numbers")

    def __del__(self):
        if hasattr(self, 'conn'): self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChemistrySimulator(root)
    root.mainloop()