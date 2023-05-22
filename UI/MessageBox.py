import tkinter as tk
from tkinter import messagebox

class CustomMessageBox:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(self.title, self.message)
        root.destroy()
message_box = CustomMessageBox("Ati depasit numarul maxim de pauze!", "Numarul maxim de pauze este 16")
message_box.show()
