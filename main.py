import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import Canvas
from datetime import datetime
from collections import Counter
import re

class ChemistrySimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("⚗️ Chemistry Experiment Simulator")
        self.root.geometry("1150x850")
        self.root.configure(bg='#f8f9fa')
        self.is_dark = False
        
        # Database connection
        try:
            self.conn = sqlite3.connect('chemistry.db')
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not connect to database: {e}")
            
        self.score = 0
        self.total_attempts = 0
        
        self.create_ui()

    def create_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#2563eb', height=110)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title = tk.Label(header_frame, text="⚗️ Chemistry Experiment Simulator",
                        font=("Segoe UI", 28, "bold"), bg='#2563eb', fg='#ffffff')
        title.pack(pady=18)
        
        subtitle = tk.Label(header_frame, text="Balance Chemical Equations & Explore Reactions",
                            font=("Segoe UI", 12), bg='#2563eb', fg='#dbeafe')
        subtitle.pack()

        # Score Bar
        score_bar = tk.Frame(self.root, bg='#f1f5f9', height=40)
        score_bar.pack(fill=tk.X, padx=30, pady=(0, 5))
        score_bar.pack_propagate(False)
        
        self.score_label = tk.Label(score_bar, text="Score: 0 | Accuracy: 0%", 
                                   font=("Segoe UI", 12, "bold"), bg='#f1f5f9', fg='#1e40af')
        self.score_label.pack(side=tk.LEFT, padx=15)

        # Theme Button Bar
        top_bar = tk.Frame(self.root, bg='#f1f5f9')
        top_bar.pack(fill=tk.X, padx=30, pady=(0, 8))

        self.theme_btn = tk.Button(top_bar, text="🌙 Dark Mode", font=("Segoe UI", 10),
                                  bg="#334155", fg="white", command=self.toggle_theme)
        self.theme_btn.pack(side=tk.RIGHT, padx=10)

        # Main content
        content_frame = tk.Frame(self.root, bg='#f8f9fa')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        self.notebook = ttk.Notebook(content_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create tabs
        self.create_combination_tab()
        self.create_double_displacement_tab()

    def create_combination_tab(self):
        tab = tk.Frame(self.notebook, bg='#f8f9fa')
        self.notebook.add(tab, text="🔬 Combination Reactions")
        
        main_container = tk.Frame(tab, bg='#f8f9fa')
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Left Panel - Input
        left_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        tk.Label(left_panel, text="🔬 Enter Reactants", font=("Segoe UI", 18, "bold"), 
                bg='#ffffff', fg='#1e40af').pack(anchor=tk.W, padx=20, pady=(20, 10))
        
        tk.Frame(left_panel, bg='#e0e7ff', height=2).pack(fill=tk.X, padx=20, pady=(0, 20))
        
        input_container = tk.Frame(left_panel, bg='#ffffff')
        input_container.pack(fill=tk.X, padx=20, pady=10)
        
        # Reactant 1
        left_group = tk.Frame(input_container, bg='#ffffff')
        left_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(left_group, text="Reactant 1", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0,5))
        tk.Label(left_group, text="Symbol:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant1_symbol = tk.Entry(left_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.comb_reactant1_symbol.pack(fill=tk.X, pady=(0,10))
        tk.Label(left_group, text="Coefficient:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant1_coeff = tk.Entry(left_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.comb_reactant1_coeff.pack(fill=tk.X)
        
        # Plus
        tk.Label(input_container, text="➕", font=("Segoe UI", 26), bg='#ffffff', fg='#2563eb').pack(side=tk.LEFT, padx=25, pady=30)
        
        # Reactant 2
        right_group = tk.Frame(input_container, bg='#ffffff')
        right_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(right_group, text="Reactant 2", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0,5))
        tk.Label(right_group, text="Symbol:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant2_symbol = tk.Entry(right_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.comb_reactant2_symbol.pack(fill=tk.X, pady=(0,10))
        tk.Label(right_group, text="Coefficient:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.comb_reactant2_coeff = tk.Entry(right_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.comb_reactant2_coeff.pack(fill=tk.X)
        
        # Buttons
        button_frame = tk.Frame(left_panel, bg='#ffffff')
        button_frame.pack(fill=tk.X, padx=20, pady=25)
        
        tk.Button(button_frame, text="⚡ React", font=("Segoe UI", 14, "bold"), 
                bg='#2563eb', fg='white', pady=12, relief=tk.FLAT,
                command=self.perform_combination_reaction).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,8))
        
        tk.Button(button_frame, text="🗑️ Clear", font=("Segoe UI", 12), 
                bg='#64748b', fg='white', pady=12, relief=tk.FLAT,
                command=self.clear_combination).pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Right Panel
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
        
        # Left Panel
        left_panel = tk.Frame(main_container, bg='#ffffff', relief=tk.RAISED, bd=1)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        tk.Label(left_panel, text="💥 Enter Compounds", font=("Segoe UI", 18, "bold"), 
                bg='#ffffff', fg='#1e40af').pack(anchor=tk.W, padx=20, pady=(20, 10))
        tk.Frame(left_panel, bg='#e0e7ff', height=2).pack(fill=tk.X, padx=20, pady=(0, 20))
        
        input_container = tk.Frame(left_panel, bg='#ffffff')
        input_container.pack(fill=tk.X, padx=20, pady=10)
        
        # Compound 1
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
        
        # Compound 2
        right_group = tk.Frame(input_container, bg='#ffffff')
        right_group.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(right_group, text="Compound 2", font=("Segoe UI", 11, "bold"), bg='#ffffff', fg='#1e293b').pack(anchor=tk.W, pady=(0,5))
        tk.Label(right_group, text="Name:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant2_symbol = tk.Entry(right_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.dd_reactant2_symbol.pack(fill=tk.X, pady=(0,10))
        tk.Label(right_group, text="Coefficient:", bg='#ffffff', fg='#475569').pack(anchor=tk.W)
        self.dd_reactant2_coeff = tk.Entry(right_group, font=("Segoe UI", 12), bg='#f1f5f9', relief=tk.FLAT)
        self.dd_reactant2_coeff.pack(fill=tk.X)
        
        # Buttons
        button_frame = tk.Frame(left_panel, bg='#ffffff')
        button_frame.pack(fill=tk.X, padx=20, pady=25)
        
        tk.Button(button_frame, text="⚡ React", font=("Segoe UI", 14, "bold"), 
                bg='#2563eb', fg='white', pady=12, relief=tk.FLAT,
                command=self.perform_double_displacement_reaction).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,8))
        
        tk.Button(button_frame, text="🗑️ Clear", font=("Segoe UI", 12), 
                bg='#64748b', fg='white', pady=12, relief=tk.FLAT,
                command=self.clear_double_displacement).pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Right Panel
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
                # Fetch original names for balancing
                self.cursor.execute("SELECT name FROM Reactants WHERE LOWER(name) = ?", (r1,))
                orig_r1 = self.cursor.fetchone()[0]
                self.cursor.execute("SELECT name FROM Reactants WHERE LOWER(name) = ?", (r2,))
                orig_r2 = self.cursor.fetchone()[0]
                balanced = self.balance_equation(orig_r1, orig_r2, prod_name)
                if balanced:
                    c1, c2, cp = balanced
                    self.comb_equation_label.config(text=f"{c1}{orig_r1} + {c2}{orig_r2} → {cp}{prod_name}")
                    self.display_color(color, self.comb_color_canvas, self.comb_product_label)
                    if user_c1 == c1 and user_c2 == c2:
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
                if user_c1 == c1 and user_c2 == c2:
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