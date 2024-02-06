import random

import string
import tkinter as tk
from tkinter import Label, Entry, Checkbutton, Button, StringVar,PhotoImage

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd

def generate_and_display_password(length_entry, numbers_var, special_var, result_label):
    min_length = int(length_entry.get())
    has_numbers = numbers_var.get() == "1"
    has_special = special_var.get() == "1"

    password = generate_password(min_length, has_numbers, has_special)

    result_label.config(text="Generated Password: " + password)

def generate_password_gui():
    window = tk.Tk()
    window.title("Password Generator")

    window.geometry("500x450")

    img_path =r"C:\Users\imanc\Desktop\Projects\Password Generator\Icon\password.png"
    original_img = PhotoImage(file=img_path)

    resized_img = original_img.subsample(2,2)

    img_label = Label(window, image=resized_img)
    img_label.pack()

    label_font = ("Arial",16)

    length_label = Label(window, text="Enter the minimum length:",font=label_font)
    length_label.pack()

    entry_button_font=("Arial",10)

    length_entry = Entry(window,font=entry_button_font)
    length_entry.pack()

    numbers_var = StringVar()
    numbers_checkbox = Checkbutton(window, text="Include Numbers", variable=numbers_var)
    numbers_checkbox.pack()

    special_var = StringVar()
    special_checkbox = Checkbutton(window, text="Include Special Characters", variable=special_var)
    special_checkbox.pack()

    generate_button = Button(window, text="Generate Password", command=lambda: generate_and_display_password(length_entry, numbers_var, special_var, result_label))
    generate_button.pack()

    result_label_font =("Arial",16)

    result_label = Label(window, text="",font=result_label_font)
    result_label.pack()

    window.mainloop()

generate_password_gui()
