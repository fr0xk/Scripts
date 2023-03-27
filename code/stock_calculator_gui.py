import tkinter as tk
from tkinter import messagebox


class StockCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Calculator")

        entries = [
            ("Beginning Year:", tk.Entry(root)),
            ("Ending Year:", tk.Entry(root)),
            ("Company Name:", tk.Entry(root)),
        ] + [("EPS {}: ".format(i+1), tk.Entry(root)) for i in range(10)] + \
              [("Current Price:", tk.Entry(root))]

        for i, (label, entry) in enumerate(entries):
            tk.Label(root, text=label).grid(row=i, column=0, padx=5, pady=5)
            entry.grid(row=i, column=1, padx=5, pady=5)

        tk.Button(root, text="Calculate", command=lambda: self.calculate(
            *[self.validate_input(entry.get(), input_type, error_message) for (label, input_type, error_message), entry in zip(entries, self.entry_fields)]
        )).grid(row=len(entries), column=0, columnspan=2, padx=5, pady=5)

        self.entry_fields = [entry for _, entry in entries]

    def validate_input(self, input_text, input_type, error_message):
        try:
            return input_type(input_text)
        except ValueError:
            messagebox.showerror("Error", error_message)
            return None

    def calculate(self, beginning_year, ending_year, company_name, *eps_values, current_price):
        if None in (beginning_year, ending_year, company_name, *eps_values, current_price) or beginning_year > ending_year:
            return

        earnings = sum(eps_values[beginning_year-2021:ending_year-2021+1])
        inflation_adjusted_earnings = [e * (1.0 + 0.025)**(2021-beginning_year-i) for i, e in enumerate(eps_values[beginning_year-2021:ending_year-2021+1])]
        shiller_pe_ratio = current_price / (sum(inflation_adjusted_earnings))

        messagebox.showinfo("Shiller PE Ratio", "The Shiller PE Ratio for {} is {:.2f}".format(company_name, shiller_pe_ratio))
