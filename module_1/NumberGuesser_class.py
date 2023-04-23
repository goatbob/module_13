"""
program: NumberGuesser_class.py
author: kyle godwin
last date modified: 18 april 2023

Class for number guessing game with
NumberGuesser_GUI.py
"""
import tkinter as tk


class NumberGuesser:
    """NumberGuesser class"""

    def __init__(self, rand_num):
        if rand_num not in range(11):  # test random number generated is in range
            raise OutofRangeException
        self.random_number = rand_num  # random number
        self.guessed_list = []  # list for storing guessed numbers

    def guess_number(self, guess_num):
        if guess_num not in range(11):  # test guess number generated is in range
            raise OutofRangeException
        self.guessed_list.append(guess_num)  # add guessed number to guessed_list
        if self.random_number == guess_num:  # check if guessed number is correct guess, window opens if true
            win = tk.Toplevel()
            win.wm_title("You win!")

            l = tk.Label(win, text=f"Winner! {self.random_number} was correct! You guessed: {self.guessed_list}")
            l.grid(row=0, column=0)

            b = tk.Button(win, text="Okay", command=win.destroy)
            b.grid(row=1, column=0)
        return self.guessed_list  # return guessed list for output

    def get_number_list(self):  # returns guessed number list -- not used
        return self.guessed_list

    def __str__(self):  # string
        return f"{self.random_number}"

    def __repr__(self):  # representation
        return f"NumberGuesser({self.random_number})"


class OutofRangeException(Exception):
    """number between 1 and 10"""
    pass
