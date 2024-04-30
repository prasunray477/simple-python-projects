""" string_input = input("Enter a string: ")

if len(string_input) == 7:
    print(f"{string_input} is Thala for a reason.")
elif string_input.isdigit():
    sum_digits = sum(int(digit) for digit in string_input)
    if sum_digits == 7:
        print(f"{string_input} is Thala for a reason.")
    else:
        print(f"{string_input} is not Thala for a reason.")
else:
    print(f"{string_input} is not Thala for a reason.") """
    




import pygame
import tkinter as tk
from tkinter import messagebox
import random

def check_string():
    string_input = entry.get()

    if len(string_input) == 7:
        messagebox.showinfo("Result", f"{string_input} is Thala for a reason.")
    elif string_input.isdigit():
        sum_digits = sum(int(digit) for digit in string_input)
        if sum_digits == 7:
            messagebox.showinfo("Result", f"{string_input} is Thala for a reason.")
        else:
            messagebox.showinfo("Result", f"{string_input} is not Thala for a reason.")
    else:
        messagebox.showinfo("Result", f"{string_input} is not Thala for a reason.")

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\prasu\\Downloads\\Bole-Jo-Koyal-Bago-Me (mp3cut.net).mp3") 
    pygame.mixer.music.play()

def generate_glitter():
    bg_color = random.choice(['gold', 'yellow', 'orange', 'blue', 'red'])
    glitter_label.config(bg=bg_color)
    root.after(500, generate_glitter)

root = tk.Tk()
root.title("Thala Checker")

frame = tk.Frame(root)
frame.pack(padx=120, pady=150)

label = tk.Label(frame, text="Check Thala:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

button = tk.Button(frame, text="Enter", command=check_string)
button.pack(side=tk.LEFT)

# Adding glitter label
glitter_label = tk.Label(frame, font=('Helvetica', 16), text="✨", bg='gold')
glitter_label.pack(side=tk.LEFT, padx=10)

play_song()
generate_glitter()  # Start the glitter effect

root.mainloop() 