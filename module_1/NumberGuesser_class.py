"""
program: NumberGuesser_class.py
author: kyle godwin
last date modified: 12 april 2023
"""
import random
import tkinter as tk


class NumberGuesser:
    """NumberGuesser class"""

    def __init__(self, rand_num):
        self.random_number = rand_num
        self.guessed_list = []

    def guess_number(self, guess_num):
        if self.random_number == guess_num:
            win = tk.Toplevel()
            win.wm_title("Window")

            l = tk.Label(win, text="Winner!")
            l.grid(row=0, column=0)

            b = tk.Button(win, text="Okay", command=win.destroy)
            b.grid(row=1, column=0)
            return f"That's right! The number was: {self.random_number}"
        else:
            return f"{guess_num} is not the correct number"

        self.guessed_list.append(guess_num)

    def get_number_list(self):
        return self.guessed_list

    def __str__(self):
        return f"{self.random_number}"

    def __repr__(self):
        return f"NumberGuesser({self.random_number})"
