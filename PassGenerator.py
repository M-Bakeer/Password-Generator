import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer for the password length.")
        return

    selections = {
        "uppercase": uppercase_var.get(),
        "lowercase": lowercase_var.get(),
        "digits": digits_var.get(),
        "symbols": symbols_var.get()
    }

    if not any(selections.values()):
        messagebox.showerror("Invalid Selection", "You must select at least one character type.")
        return

    options = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
    starter = []
    char_pool = ""

    for i, include in enumerate(selections.values()):
        if include:
            starter.append(random.choice(options[i]))
            char_pool += options[i]

    remaining = length - len(starter)
    rest = random.choices(char_pool, k=remaining)
    password_list = starter + rest
    random.shuffle(password_list)
    password = ''.join(password_list)

    password_var.set(password)
    evaluate_strength(length, sum(selections.values()))

def evaluate_strength(length, selected_types):
    if length < 8 or selected_types == 1:
        strength_label.config(text="Strength: Weak ⚠️", fg="red")
    elif length < 12 or selected_types < 4:
        strength_label.config(text="Strength: Moderate ⚠️", fg="orange")
    else:
        strength_label.config(text="Strength: Strong ✅", fg="green")

def copy_to_clipboard(event=None):
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Checkboxes
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Digits", variable=digits_var).grid(row=3, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Symbols", variable=symbols_var).grid(row=4, column=0, columnspan=2, sticky="w")

tk.Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=40, justify="center", fg="blue", font=("Arial", 12))
password_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
password_entry.bind("<Button-1>", copy_to_clipboard)

strength_label = tk.Label(root, text="Strength: ", font=("Arial", 10, "italic"))
strength_label.grid(row=7, column=0, columnspan=2)

tk.Label(root, text="Click the password to copy it.").grid(row=8, column=0, columnspan=2, pady=5)

root.mainloop()
