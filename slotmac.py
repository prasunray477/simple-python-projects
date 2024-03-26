import tkinter as tk
import random

def spin():
    slots = [random.randint(0,9) for _ in range(3)]
    slot_vars[0].set(slots[0])
    slot_vars[1].set(slots[1])
    slot_vars[2].set(slots[2])

    if slots[0] == slots[1] == slots[2]:
        result.set("You won!")
    else:
        result.set("You lost. Try again!")

root = tk.Tk()
root.title("Slot Machine")
root.geometry("300x200")
root.configure(bg="dark blue")

slot_vars = [tk.IntVar() for _ in range(3)]
result = tk.StringVar()

for i in range(3):
    tk.Label(root, textvariable=slot_vars[i], font=("Helvetica", 24), bg="dark blue", fg="red").grid(row=0, column=i)

tk.Button(root, text="Spin", command=spin, font=("Helvetica", 16), bg="green", fg="black").grid(row=1, column=1)

tk.Label(root, textvariable=result, font=("Helvetica", 16), bg="dark blue", fg="yellow").grid(row=2, column=1)

root.mainloop()