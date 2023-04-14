"""
program: NumberGuesser_class.py
author: kyle godwin
last date modified: 12 april 2023
"""
import random
import tkinter as tk


class n:
    """NumberGuesser class"""
    guessed_list = []

    def __init__(self, rand_num=0):
        if rand_num == 0:
            rand_num = random.randint(1, 10)
        self.random_number = rand_num

    def guess_number(self, num):
        if num == self.random_number:
            tk.messagebox.showinfo("Winner", "You selected the correct number!")
            # return f"That's right! The number was: {self.random_number}"
        # else:
            # return f"{num} is not the correct number"

    def add_number(self, num):
        n.guessed_list.append(num)
        return n.guessed_list

    def get_number_list(self):
        return n.guessed_list

    def __str__(self):
        return f"{self.random_number}"

    def __repr__(self):
        return f"NumberGuesser({self.random_number})"
