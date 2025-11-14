import tkinter as tk
from tkinter import ttk, messagebox

def calculate_split():
    try:
        subtotal = float(entry_subtotal.get())
        tax_percent = float(entry_tax.get())
        num_people = int(entry_people.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")
        return

    if subtotal <= 0 or num_people <= 0 or tax_percent < 0:
        messagebox.showerror("Error", "Enter valid positive values.")
        return

    tax_amount = subtotal * (tax_percent / 100)
    total_bill = subtotal + tax_amount

    has_veg = veg_var.get()
    meat_total = 0

    if has_veg:
        try:
            meat_total = float(entry_meat.get())
            veg_count = int(entry_veg_count.get())
        except ValueError:
            messagebox.showerror("Error", "Enter valid vegetarian/meat details.")
            return

        if meat_total < 0 or meat_total > subtotal:
            messagebox.showerror("Error", "Invalid meat total.")
            return

        if veg_count < 0 or veg_count >= num_people:
            messagebox.showerror("Error", "Vegetarian count must be less than total people.")
            return

    if has_veg and meat_total > 0:
        non_veg_count = num_people - veg_count

        vegetarian_items = subtotal - meat_total
        meat_per_person = meat_total / non_veg_count
        veg_items_per_person = vegetarian_items / num_people
        tax_per_person = tax_amount / num_people

        result = f"Total Bill: ${total_bill:.2f}\n"
        result += f"Vegetarian items per person: ${veg_items_per_person:.2f}\n"
        result += f"Meat items per non-veg person: ${meat_per_person:.2f}\n"
        result += f"Tax per person: ${tax_per_person:.2f}\n\n"
    else:
        per_person = total_bill / num_people
        result = (
            f"Total Bill: ${total_bill:.2f}\n"
            f"Each person pays: ${per_person:.2f}\n"
        )

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

def toggle_meat_fields():
    if veg_var.get():
        meat_frame.pack(fill="x", pady=10)
    else:
        meat_frame.pack_forget()

root = tk.Tk()
root.title("Bill Splitter")
root.geometry("520x720")
root.configure(bg="#f5f5f5")

main = ttk.Frame(root, padding=25)
main.pack(fill="both", expand=True)

title = ttk.Label(main, text="Bill Splitter", font=("Arial", 24, "bold"))
title.pack(pady=15)

frm_inputs = ttk.Frame(main, padding=10)
frm_inputs.pack(fill="x", pady=10)

lbl_subtotal = ttk.Label(frm_inputs, text="Subtotal (before tax):")
lbl_subtotal.grid(row=0, column=0, sticky="w", pady=10)
entry_subtotal = ttk.Entry(frm_inputs, width=28)
entry_subtotal.grid(row=0, column=1, pady=10)

lbl_tax = ttk.Label(frm_inputs, text="Tax Percentage:")
lbl_tax.grid(row=1, column=0, sticky="w", pady=10)
entry_tax = ttk.Entry(frm_inputs, width=28)
entry_tax.grid(row=1, column=1, pady=10)

lbl_people = ttk.Label(frm_inputs, text="Number of People:")
lbl_people.grid(row=2, column=0, sticky="w", pady=10)
entry_people = ttk.Entry(frm_inputs, width=28)
entry_people.grid(row=2, column=1, pady=10)

veg_var = tk.IntVar()
chk_veg = ttk.Checkbutton(main, text="Are there vegetarians?", variable=veg_var, command=toggle_meat_fields)
chk_veg.pack(pady=10)

meat_frame = ttk.Frame(main, padding=10)

lbl_meat = ttk.Label(meat_frame, text="Total Meat Items:")
lbl_meat.grid(row=0, column=0, sticky="w", pady=10)
entry_meat = ttk.Entry(meat_frame, width=28)
entry_meat.grid(row=0, column=1, pady=10)

lbl_veg_count = ttk.Label(meat_frame, text="Number of Vegetarians:")
lbl_veg_count.grid(row=1, column=0, sticky="w", pady=10)
entry_veg_count = ttk.Entry(meat_frame, width=28)
entry_veg_count.grid(row=1, column=1, pady=10)

btn_calc = ttk.Button(main, text="Calculate Bill", command=calculate_split)
btn_calc.pack(pady=20)

text_output = tk.Text(main, height=12, width=58, padx=10, pady=10, font=("Arial", 12))
text_output.pack(pady=10)

root.mainloop()
