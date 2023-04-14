"""
program: NumberGuesser_class.py
author: kyle godwin
last date modified: 12 april 2023
"""
import random
import tkinter as tk


class NumberGuesser:
    """NumberGuesser class"""
    guessed_list = []

    def __init__(self, num):
        self.random_number = num

    def guess_number(self, num):
        if num == self.random_number:
            win = tk.Toplevel()
            win.wm_title("Window")

            l = tk.Label(win, text="Winner!")
            l.grid(row=0, column=0)

            b = tk.Button(win, text="Okay", command=win.destroy)
            b.grid(row=1, column=0)
            # return f"That's right! The number was: {self.random_number}"
        # else:
            # return f"{num} is not the correct number"

    def add_number(self, num):
        NumberGuesser.guessed_list.append(num)
        return NumberGuesser.guessed_list

    def get_number_list(self):
        return NumberGuesser.guessed_list

    def __str__(self):
        return f"{self.random_number}"

    def __repr__(self):
        return f"NumberGuesser({self.random_number})"
