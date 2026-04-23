import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import Canvas

class ChemistrySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("⚗️ Chemistry Experiment Simulator")
        self.root.geometry("1100x800")
        self.root.configure(bg='#f8f9fa')
        
        # Database connection
        self.conn = sqlite3.connect('chemistry.db')
        self.cursor = self.conn.cursor()
        
        # Create main UI
        self.create_ui()
        
    def create_ui(self):
        """Create the main UI with tabs"""
        
        # Header
        header_frame = tk.Frame(self.root, bg='#2563eb', height=100)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title = tk.Label(
            header_frame,
            text="⚗️ Chemistry Experiment Simulator",
            font=("Segoe UI", 28, "bold"),
            bg='#2563eb',
            fg='#ffffff'
        )
        title.pack(pady=15)
        
        subtitle = tk.Label(
            header_frame,
            text="Balance Chemical Equations & Explore Reactions",
            font=("Segoe UI", 12),
            bg='#2563eb',
            fg='#dbeafe'
        )
        subtitle.pack()
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg='#f8f9fa')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(content_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Style for notebook
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='#f8f9fa', borderwidth=0)
        style.configure('TNotebook.Tab', padding=[20, 10], font=("Segoe UI", 11))
        style.map('TNotebook.Tab',
                  background=[("selected", '#ffffff'), ("", '#e5e7eb')],
                  foreground=[("selected", '#1e40af'), ("", '#475569')])
        
        # Create tabs
        self.create_combination_tab()
        self.create_double_displacement_tab()
        
    def create_combination_tab(self):
        """Create Combination Reaction tab"""
        
        tab = tk.Frame(self.notebook, bg='#f8f9fa')
        self.notebook.add(tab, text="🔬 Combination Reactions")
        
        # Main container with two panels
        main_container = tk.Frame(tab, bg='#f8f9fa')
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # ===== LEFT PANEL - INPUT =====
        left_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        # Title
        input_title = tk.Label(
            left_panel,
            text="🔬 Enter Reactants",
            font=("Segoe UI", 18, "bold"),
            bg='#ffffff',
            fg='#1e40af'
        )
        input_title.pack(anchor=tk.W, padx=20, pady=(20, 10))
        
        # Separator
        separator1 = tk.Frame(left_panel, bg='#e0e7ff', height=2)
        separator1.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Input fields container - HORIZONTAL LAYOUT
        input_container = tk.Frame(left_panel, bg='#ffffff')
        input_container.pack(fill=tk.X, padx=20, pady=10)
        
        # Left input group
        left_input_group = tk.Frame(input_container, bg='#ffffff')
        left_input_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(left_input_group, text="Reactant 1", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0, 5))
        tk.Label(left_input_group, text="Symbol:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant1_symbol = tk.Entry(left_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=10)
        self.comb_reactant1_symbol.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(left_input_group, text="Coefficient:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant1_coeff = tk.Entry(left_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=10)
        self.comb_reactant1_coeff.pack(fill=tk.X)
        
        # Plus sign in middle
        plus_frame = tk.Frame(input_container, bg='#ffffff')
        plus_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20)
        tk.Label(plus_frame, text="➕", font=("Segoe UI", 24), bg='#ffffff', fg='#2563eb').pack(pady=20)
        
        # Right input group
        right_input_group = tk.Frame(input_container, bg='#ffffff')
        right_input_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(right_input_group, text="Reactant 2", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0, 5))
        tk.Label(right_input_group, text="Symbol:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant2_symbol = tk.Entry(right_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=10)
        self.comb_reactant2_symbol.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(right_input_group, text="Coefficient:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant2_coeff = tk.Entry(right_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=10)
        self.comb_reactant2_coeff.pack(fill=tk.X)
        
        # React Button
        button_frame = tk.Frame(left_panel, bg='#ffffff')
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        self.comb_react_button = tk.Button(
            button_frame,
            text="⚡ React",
            font=("Segoe UI", 14, "bold"),
            bg='#2563eb',
            fg='#ffffff',
            padx=40,
            pady=12,
            border=0,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.perform_combination_reaction,
            activebackground='#1d4ed8',
            activeforeground='#ffffff'
        )
        self.comb_react_button.pack(fill=tk.X)
        
        # ===== RIGHT PANEL - RESULTS =====
        right_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(15, 0))
        
        # Title
        result_title = tk.Label(
            right_panel,
            text="📊 Reaction Result",
            font=("Segoe UI", 18, "bold"),
            bg='#ffffff',
            fg='#1e40af'
        )
        result_title.pack(anchor=tk.W, padx=20, pady=(20, 10))
        
        # Separator
        separator2 = tk.Frame(right_panel, bg='#e0e7ff', height=2)
        separator2.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Equation display
        tk.Label(right_panel, text="Balanced Equation:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(0, 5))
        equation_frame = tk.Frame(right_panel, bg='#dbeafe', relief=tk.FLAT, bd=0)
        equation_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self.comb_equation_label = tk.Label(
            equation_frame,
            text="(Enter reactants and press React)",
            font=("Courier New", 13, "bold"),
            bg='#dbeafe',
            fg='#0c4a6e',
            wraplength=350,
            pady=10,
            padx=10
        )
        self.comb_equation_label.pack(fill=tk.BOTH)
        
        # Correction message
        tk.Label(right_panel, text="Correction:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(15, 5))
        self.comb_correction_label = tk.Label(
            right_panel,
            text="",
            font=("Segoe UI", 10),
            bg='#ffffff',
            fg='#059669',
            wraplength=350,
            justify=tk.LEFT
        )
        self.comb_correction_label.pack(anchor=tk.W, padx=20, pady=(0, 15))
        
        # Product color display
        tk.Label(right_panel, text="Product Color:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(0, 5))
        
        color_display_frame = tk.Frame(right_panel, bg='#ffffff')
        color_display_frame.pack(anchor=tk.W, padx=20, pady=(0, 15))
        
        self.comb_color_canvas = Canvas(color_display_frame, width=100, height=60, bg='#ffffff', highlightthickness=1, highlightbackground='#cbd5e1')
        self.comb_color_canvas.pack(side=tk.LEFT, padx=(0, 10))
        
        self.comb_product_label = tk.Label(
            color_display_frame,
            text="",
            font=("Segoe UI", 12, "bold"),
            bg='#ffffff',
            fg='#1e293b'
        )
        self.comb_product_label.pack(side=tk.LEFT, anchor=tk.W)
        
        # Status message
        self.comb_status_label = tk.Label(
            right_panel,
            text="",
            font=("Segoe UI", 10),
            bg='#ffffff',
            fg='#059669',
            wraplength=350,
            justify=tk.LEFT
        )
        self.comb_status_label.pack(anchor=tk.W, padx=20, pady=20, fill=tk.BOTH, expand=True)
    
    def create_double_displacement_tab(self):
        """Create Double Displacement Reaction tab"""
        
        tab = tk.Frame(self.notebook, bg='#f8f9fa')
        self.notebook.add(tab, text="💥 Double Displacement (Precipitation)")
        
        # Main container with two panels
        main_container = tk.Frame(tab, bg='#f8f9fa')
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # ===== LEFT PANEL - INPUT =====
        left_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        # Title
        input_title = tk.Label(
            left_panel,
            text="💥 Enter Compounds",
            font=("Segoe UI", 18, "bold"),
            bg='#ffffff',
            fg='#1e40af'
        )
        input_title.pack(anchor=tk.W, padx=20, pady=(20, 10))
        
        # Separator
        separator1 = tk.Frame(left_panel, bg='#e0e7ff', height=2)
        separator1.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Input fields container - HORIZONTAL LAYOUT
        input_container = tk.Frame(left_panel, bg='#ffffff')
        input_container.pack(fill=tk.X, padx=20, pady=10)
        
        # Left input group
        left_input_group = tk.Frame(input_container, bg='#ffffff')
        left_input_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(left_input_group, text="Compound 1", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0, 5))
        tk.Label(left_input_group, text="Name:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant1_symbol = tk.Entry(left_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=12)
        self.dd_reactant1_symbol.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(left_input_group, text="Coefficient:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant1_coeff = tk.Entry(left_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=12)
        self.dd_reactant1_coeff.pack(fill=tk.X)
        
        # Plus sign in middle
        plus_frame = tk.Frame(input_container, bg='#ffffff')
        plus_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20)
        tk.Label(plus_frame, text="➕", font=("Segoe UI", 24), bg='#ffffff', fg='#2563eb').pack(pady=20)
        
        # Right input group
        right_input_group = tk.Frame(input_container, bg='#ffffff')
        right_input_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(right_input_group, text="Compound 2", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0, 5))
        tk.Label(right_input_group, text="Name:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant2_symbol = tk.Entry(right_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=12)
        self.dd_reactant2_symbol.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(right_input_group, text="Coefficient:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant2_coeff = tk.Entry(right_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=12)
        self.dd_reactant2_coeff.pack(fill=tk.X)
        
        # React Button
        button_frame = tk.Frame(left_panel, bg='#ffffff')
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        self.dd_react_button = tk.Button(
            button_frame,
            text="⚡ React",
            font=("Segoe UI", 14, "bold"),
            bg='#2563eb',
            fg='#ffffff',
            padx=40,
            pady=12,
            border=0,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.perform_double_displacement_reaction,
            activebackground='#1d4ed8',
            activeforeground='#ffffff'
        )
        self.dd_react_button.pack(fill=tk.X)
        
        # ===== RIGHT PANEL - RESULTS =====
        right_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(15, 0))
        
        # Title
        result_title = tk.Label(
            right_panel,
            text="📊 Reaction Result",
            font=("Segoe UI", 18, "bold"),
            bg='#ffffff',
            fg='#1e40af'
        )
        result_title.pack(anchor=tk.W, padx=20, pady=(20, 10))
        
        # Separator
        separator2 = tk.Frame(right_panel, bg='#e0e7ff', height=2)
        separator2.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Equation display
        tk.Label(right_panel, text="Balanced Equation:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(0, 5))
        equation_frame = tk.Frame(right_panel, bg='#dbeafe', relief=tk.FLAT, bd=0)
        equation_frame.pack(fill=tk.X, padx=20, pady=(0, 15))
        
        self.dd_equation_label = tk.Label(
            equation_frame,
            text="(Enter compounds and press React)",
            font=("Courier New", 13, "bold"),
            bg='#dbeafe',
            fg='#0c4a6e',
            wraplength=350,
            pady=10,
            padx=10
        )
        self.dd_equation_label.pack(fill=tk.BOTH)
        
        # Precipitate info
        tk.Label(right_panel, text="Precipitate Formed:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(15, 5))
        self.dd_precipitate_label = tk.Label(
            right_panel,
            text="",
            font=("Segoe UI", 10),
            bg='#ffffff',
            fg='#dc2626',
            wraplength=350,
            justify=tk.LEFT
        )
        self.dd_precipitate_label.pack(anchor=tk.W, padx=20, pady=(0, 15))
        
        # Precipitate color display
        tk.Label(right_panel, text="Precipitate Color:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(0, 5))
        
        color_display_frame = tk.Frame(right_panel, bg='#ffffff')
        color_display_frame.pack(anchor=tk.W, padx=20, pady=(0, 15))
        
        self.dd_color_canvas = Canvas(color_display_frame, width=100, height=60, bg='#ffffff', highlightthickness=1, highlightbackground='#cbd5e1')
        self.dd_color_canvas.pack(side=tk.LEFT, padx=(0, 10))
        
        self.dd_color_label = tk.Label(
            color_display_frame,
            text="",
            font=("Segoe UI", 12, "bold"),
            bg='#ffffff',
            fg='#1e293b'
        )
        self.dd_color_label.pack(side=tk.LEFT, anchor=tk.W)
        
        # Status message
        self.dd_status_label = tk.Label(
            right_panel,
            text="",
            font=("Segoe UI", 10),
            bg='#ffffff',
            fg='#059669',
            wraplength=350,
            justify=tk.LEFT
        )
        self.dd_status_label.pack(anchor=tk.W, padx=20, pady=20, fill=tk.BOTH, expand=True)
    
    def get_compound_composition(self, compound_name):
        """Get the composition of a compound from database"""
        self.cursor.execute("""
            SELECT element_symbol, count FROM Compound_Composition
            WHERE compound_name = ?
        """, (compound_name,))
        
        result = self.cursor.fetchall()
        if result:
            return {element: count for element, count in result}
        return None
    
    def balance_equation(self, reactant1_symbol, reactant2_symbol, product_symbol):
        """Try to balance the equation automatically"""
        
        # Get compositions
        r1_comp = self.get_compound_composition(reactant1_symbol)
        r2_comp = self.get_compound_composition(reactant2_symbol)
        prod_comp = self.get_compound_composition(product_symbol)
        
        # If any is a simple element, treat as single element
        if r1_comp is None:
            r1_comp = {reactant1_symbol: 1}
        if r2_comp is None:
            r2_comp = {reactant2_symbol: 1}
        if prod_comp is None:
            prod_comp = {product_symbol: 1}
        
        # Try coefficients from 1 to 10
        for coeff1 in range(1, 11):
            for coeff2 in range(1, 11):
                for coeff_prod in range(1, 11):
                    # Count atoms on left side
                    left_atoms = {}
                    for elem, count in r1_comp.items():
                        left_atoms[elem] = left_atoms.get(elem, 0) + count * coeff1
                    for elem, count in r2_comp.items():
                        left_atoms[elem] = left_atoms.get(elem, 0) + count * coeff2
                    
                    # Count atoms on right side
                    right_atoms = {}
                    for elem, count in prod_comp.items():
                        right_atoms[elem] = right_atoms.get(elem, 0) + count * coeff_prod
                    
                    # Check if balanced
                    if left_atoms == right_atoms:
                        return coeff1, coeff2, coeff_prod
        
        return None
    
    def perform_combination_reaction(self):
        """Perform combination reaction"""
        
        try:
            reactant1_symbol = self.comb_reactant1_symbol.get().strip()
            reactant2_symbol = self.comb_reactant2_symbol.get().strip()
            user_coeff1 = self.comb_reactant1_coeff.get().strip()
            user_coeff2 = self.comb_reactant2_coeff.get().strip()
            
            if not reactant1_symbol or not reactant2_symbol:
                messagebox.showerror("Error", "Please enter both reactant symbols")
                return
            
            user_coeff1 = int(user_coeff1) if user_coeff1 else 1
            user_coeff2 = int(user_coeff2) if user_coeff2 else 1
            
            # Query database
            self.cursor.execute("""
                SELECT r.equation, p.name, p.color, r.reaction_type
                FROM Reactions r
                JOIN Products p ON r.product_id = p.id
                JOIN Reaction_Reactants rr ON r.id = rr.reaction_id
                JOIN Reactants reactants ON rr.reactant_id = reactants.id
                WHERE reactants.name IN (?, ?)
                AND r.reaction_type = 'Combination'
                GROUP BY r.id
                HAVING COUNT(DISTINCT reactants.id) = 2
            """, (reactant1_symbol, reactant2_symbol))
            
            result = self.cursor.fetchone()
            
            if result:
                equation, product_name, color, reaction_type = result
                
                balanced = self.balance_equation(reactant1_symbol, reactant2_symbol, product_name)
                
                if balanced:
                    correct_coeff1, correct_coeff2, correct_prod = balanced
                    balanced_equation = f"{correct_coeff1}{reactant1_symbol} + {correct_coeff2}{reactant2_symbol} → {correct_prod}{product_name}"
                    
                    self.comb_equation_label.config(text=balanced_equation, fg='#0c4a6e')
                    self.comb_product_label.config(text=f"Product: {product_name}", fg='#1e293b')
                    self.display_color(color, self.comb_color_canvas, self.comb_product_label)
                    
                    if user_coeff1 == correct_coeff1 and user_coeff2 == correct_coeff2:
                        self.comb_correction_label.config(text="✓ Your coefficients are correct!", fg='#059669')
                        self.comb_status_label.config(text="🎉 Perfect! The equation is balanced correctly!", fg='#059669')
                    else:
                        correction_text = f"⚠ Your coefficients: {user_coeff1}, {user_coeff2}\n✓ Correct: {correct_coeff1}, {correct_coeff2}"
                        self.comb_correction_label.config(text=correction_text, fg='#d97706')
                        self.comb_status_label.config(text="The equation has been auto-balanced.", fg='#d97706')
                else:
                    self.comb_equation_label.config(text="Could not balance", fg='#dc2626')
                    self.comb_status_label.config(text="❌ Unable to balance", fg='#dc2626')
            else:
                self.comb_equation_label.config(text="No reaction occurs", fg='#dc2626')
                self.comb_product_label.config(text="", fg='#1e293b')
                self.comb_color_canvas.delete("all")
                self.comb_status_label.config(text="❌ No matching reaction found", fg='#dc2626')
                
        except ValueError:
            messagebox.showerror("Error", "Coefficients must be numbers")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
    
    def perform_double_displacement_reaction(self):
        """Perform double displacement reaction"""
        
        try:
            reactant1_name = self.dd_reactant1_symbol.get().strip()
            reactant2_name = self.dd_reactant2_symbol.get().strip()
            user_coeff1 = self.dd_reactant1_coeff.get().strip()
            user_coeff2 = self.dd_reactant2_coeff.get().strip()
            
            if not reactant1_name or not reactant2_name:
                messagebox.showerror("Error", "Please enter both compound names")
                return
            
            user_coeff1 = int(user_coeff1) if user_coeff1 else 1
            user_coeff2 = int(user_coeff2) if user_coeff2 else 1
            
            # Query database
            self.cursor.execute("""
                SELECT r.equation, p.name, p.color
FROM Reactions r
JOIN Products p ON r.product_id = p.id
JOIN Reaction_Reactants rr ON r.id = rr.reaction_id
JOIN Reactants reactants ON rr.reactant_id = reactants.id
WHERE r.reaction_type = 'Double Displacement'
GROUP BY r.id
HAVING 
    SUM(CASE WHEN LOWER(reactants.name) = LOWER(?) THEN 1 ELSE 0 END) > 0
AND 
    SUM(CASE WHEN LOWER(reactants.name) = LOWER(?) THEN 1 ELSE 0 END) > 0
            """, (reactant1_name, reactant2_name))
            
            result = self.cursor.fetchone()
            
            if result:
                equation, product_name, color, reaction_type = result
                
                self.dd_equation_label.config(text=equation, fg='#0c4a6e')
                self.dd_precipitate_label.config(text=f"↓ {product_name} (Precipitate)", fg='#dc2626')
                self.display_color(color, self.dd_color_canvas, self.dd_color_label)
                self.dd_status_label.config(text="✓ Precipitation reaction successful! A solid has formed.", fg='#059669')
            else:
                self.dd_equation_label.config(text="No reaction occurs", fg='#dc2626')
                self.dd_precipitate_label.config(text="", fg='#dc2626')
                self.dd_color_canvas.delete("all")
                self.dd_status_label.config(text="❌ These compounds don't form a precipitation reaction", fg='#dc2626')
                
        except ValueError:
            messagebox.showerror("Error", "Coefficients must be numbers")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
    
    def display_color(self, color_name, canvas, label):
        """Display color on canvas"""
        
        canvas.delete("all")
        
        color_map = {
            'White': '#ffffff',
            'Colorless': '#e0e7ff',
            'Red-Brown': '#b91c1c',
            'Reddish-Brown': '#d2691e',
            'Gray-White': '#d1d5db',
            'Yellow': '#fbbf24',
            'Black': '#1f2937',
        }
        
        hex_color = color_map.get(color_name, '#cbd5e1')
        
        canvas.create_rectangle(2, 2, 98, 58, fill=hex_color, outline='#cbd5e1', width=2)
        text_color = '#1f2937' if color_name not in ['Colorless', 'White'] else '#0c4a6e'
        canvas.create_text(50, 30, text=color_name, font=("Segoe UI", 9, "bold"), fill=text_color)
        
        label.config(text=color_name)

def main():
    root = tk.Tk()
    app = ChemistrySimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()