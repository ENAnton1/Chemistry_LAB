import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import Canvas
from itertools import product

class ChemistrySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("⚗️ Chemistry Experiment Simulator")
        self.root.geometry("1000x750")
        self.root.configure(bg='#f8f9fa')
        
        # Database connection
        self.conn = sqlite3.connect('chemistry.db')
        self.cursor = self.conn.cursor()
        
        # Create main UI
        self.create_ui()
        
    def create_ui(self):
        """Create the main UI"""
        
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
        
        # Create combination reaction tab
        self.create_combination_tab(content_frame)
        
    def create_combination_tab(self, parent):
        """Create Combination Reaction interface"""
        
        # Main container with two panels
        main_container = tk.Frame(parent, bg='#f8f9fa')
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
        self.reactant1_symbol = tk.Entry(left_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=10)
        self.reactant1_symbol.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(left_input_group, text="Coefficient:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.reactant1_coeff = tk.Entry(left_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=10)
        self.reactant1_coeff.pack(fill=tk.X)
        
        # Plus sign in middle
        plus_frame = tk.Frame(input_container, bg='#ffffff')
        plus_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20)
        tk.Label(plus_frame, text="➕", font=("Segoe UI", 24), bg='#ffffff', fg='#2563eb').pack(pady=20)
        
        # Right input group
        right_input_group = tk.Frame(input_container, bg='#ffffff')
        right_input_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(right_input_group, text="Reactant 2", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0, 5))
        tk.Label(right_input_group, text="Symbol:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.reactant2_symbol = tk.Entry(right_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=10)
        self.reactant2_symbol.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(right_input_group, text="Coefficient:", font=("Segoe UI", 10), bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.reactant2_coeff = tk.Entry(right_input_group, font=("Segoe UI", 12), bg='#f1f5f9', fg='#1e293b', relief=tk.FLAT, width=10)
        self.reactant2_coeff.pack(fill=tk.X)
        
        # React Button
        button_frame = tk.Frame(left_panel, bg='#ffffff')
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        self.react_button = tk.Button(
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
            command=self.perform_reaction,
            activebackground='#1d4ed8',
            activeforeground='#ffffff'
        )
        self.react_button.pack(fill=tk.X)
        
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
        
        self.equation_label = tk.Label(
            equation_frame,
            text="(Enter reactants and press React)",
            font=("Courier New", 13, "bold"),
            bg='#dbeafe',
            fg='#0c4a6e',
            wraplength=350,
            pady=10,
            padx=10
        )
        self.equation_label.pack(fill=tk.BOTH)
        
        # Correction message
        tk.Label(right_panel, text="Correction:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(15, 5))
        self.correction_label = tk.Label(
            right_panel,
            text="",
            font=("Segoe UI", 10),
            bg='#ffffff',
            fg='#059669',
            wraplength=350,
            justify=tk.LEFT
        )
        self.correction_label.pack(anchor=tk.W, padx=20, pady=(0, 15))
        
        # Product color display
        tk.Label(right_panel, text="Product Color:", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, padx=20, pady=(0, 5))
        
        color_display_frame = tk.Frame(right_panel, bg='#ffffff')
        color_display_frame.pack(anchor=tk.W, padx=20, pady=(0, 15))
        
        self.color_canvas = Canvas(color_display_frame, width=100, height=60, bg='#ffffff', highlightthickness=1, highlightbackground='#cbd5e1')
        self.color_canvas.pack(side=tk.LEFT, padx=(0, 10))
        
        self.product_label = tk.Label(
            color_display_frame,
            text="",
            font=("Segoe UI", 12, "bold"),
            bg='#ffffff',
            fg='#1e293b'
        )
        self.product_label.pack(side=tk.LEFT, anchor=tk.W)
        
        # Status message
        self.status_label = tk.Label(
            right_panel,
            text="",
            font=("Segoe UI", 10),
            bg='#ffffff',
            fg='#059669',
            wraplength=350,
            justify=tk.LEFT
        )
        self.status_label.pack(anchor=tk.W, padx=20, pady=20, fill=tk.BOTH, expand=True)
        
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
        
        # If any is a simple element (not in database), treat as single element
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
    
    def perform_reaction(self):
        """Perform the chemical reaction with balancing"""
        
        try:
            # Get input values
            reactant1_symbol = self.reactant1_symbol.get().strip()
            reactant2_symbol = self.reactant2_symbol.get().strip()
            user_coeff1 = self.reactant1_coeff.get().strip()
            user_coeff2 = self.reactant2_coeff.get().strip()
            
            # Validate inputs
            if not reactant1_symbol or not reactant2_symbol:
                messagebox.showerror("Error", "Please enter both reactant symbols")
                return
            
            # Convert user coefficients
            user_coeff1 = int(user_coeff1) if user_coeff1 else 1
            user_coeff2 = int(user_coeff2) if user_coeff2 else 1
            
            # Query database for reaction
            self.cursor.execute("""
                        SELECT r.equation, p.name, p.color, r.reaction_type
                        FROM Reactions r
                        JOIN Products p ON r.product_id = p.id
                        JOIN Reaction_Reactants rr ON r.id = rr.reaction_id
                        JOIN Reactants reactants ON rr.reactant_id = reactants.id
                        WHERE reactants.name IN (?, ?)
                        GROUP BY r.id
                        HAVING COUNT(DISTINCT reactants.id) = 2
                        LIMIT 1
                            """, 
                    (reactant1_symbol, reactant2_symbol))
            
            result = self.cursor.fetchone()
            
            if result:
                equation, product_name, color, reaction_type = result
                
                # Try to balance the equation
                balanced = self.balance_equation(reactant1_symbol, reactant2_symbol, product_name)
                
                if balanced:
                    correct_coeff1, correct_coeff2, correct_prod = balanced
                    
                    # Create balanced equation
                    balanced_equation = f"{correct_coeff1}{reactant1_symbol} + {correct_coeff2}{reactant2_symbol} → {correct_prod}{product_name}"
                    
                    # Display equation
                    self.equation_label.config(text=balanced_equation, fg='#0c4a6e')
                    
                    # Display product name
                    self.product_label.config(text=f"Product: {product_name}", fg='#1e293b')
                    
                    # Display color
                    self.display_color(color)
                    
                    # Check if user coefficients are correct
                    if user_coeff1 == correct_coeff1 and user_coeff2 == correct_coeff2:
                        self.correction_label.config(text="✓ Your coefficients are correct!", fg='#059669')
                        self.status_label.config(text="🎉 Perfect! The equation is balanced correctly!", fg='#059669')
                    else:
                        correction_text = f"⚠ Your coefficients were: {user_coeff1}, {user_coeff2}\n✓ Correct coefficients: {correct_coeff1}, {correct_coeff2}"
                        self.correction_label.config(text=correction_text, fg='#d97706')
                        self.status_label.config(text="The equation has been auto-balanced. Compare with your answer!", fg='#d97706')
                else:
                    self.equation_label.config(text="Could not balance equation", fg='#dc2626')
                    self.correction_label.config(text="", fg='#059669')
                    self.status_label.config(text="❌ Unable to balance this equation", fg='#dc2626')
                
            else:
                # No reaction found
                self.equation_label.config(text="No reaction occurs", fg='#dc2626')
                self.product_label.config(text="", fg='#1e293b')
                self.color_canvas.delete("all")
                self.correction_label.config(text="", fg='#059669')
                self.status_label.config(
                    text="❌ These reactants don't form a combination reaction. Try different elements.",
                    fg='#dc2626'
                )
                
        except ValueError:
            messagebox.showerror("Error", "Coefficients must be numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def display_color(self, color_name):
        """Display the product color on canvas"""
        
        self.color_canvas.delete("all")
        
        # Map color names to hex values
        color_map = {
            'White': '#f5f5f5',
            'Colorless': '#e0f2fe',
            'Red-Brown': '#ea580c',
            'Gray-White': '#e5e7eb',
            'Yellow': '#fbbf24',
            'Black': '#1f2937',
        }
        
        hex_color = color_map.get(color_name, '#e5e7eb')
        
        # Draw color box
        self.color_canvas.create_rectangle(2, 2, 98, 58, fill=hex_color, outline='#cbd5e1', width=2)
        
        # Display color name
        text_color = '#1f2937' if color_name != 'Colorless' else '#0c4a6e'
        self.color_canvas.create_text(50, 30, text=color_name, font=("Segoe UI", 9, "bold"), fill=text_color)

def main():
    root = tk.Tk()
    app = ChemistrySimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()