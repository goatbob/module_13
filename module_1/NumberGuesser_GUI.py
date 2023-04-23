"""
program: NumberGuesser_GUI.py
author: kyle godwin
last date modified: 18 april 2023

user interface for number guessing game
utilizing NumberGuesser_class.py
"""
from NumberGuesser_class import NumberGuesser
import tkinter as tk
import random


def start_game():  # turn all guess buttons to normal
    num_1.config(state='normal')
    num_2.config(state='normal')
    num_3.config(state='normal')
    num_4.config(state='normal')
    num_5.config(state='normal')
    num_6.config(state='normal')
    num_7.config(state='normal')
    num_8.config(state='normal')
    num_9.config(state='normal')
    num_10.config(state='normal')

    rand_num = random.randint(1, 10)  # generate random number between 1 and 10
    global n
    n = NumberGuesser(rand_num)  # initialize the NumberGuesser class


def button_guess(pressed_button):  # disables guess button once pressed
    if pressed_button == 1:
        num_1.config(state="disabled")
    elif pressed_button == 2:
        num_2.config(state="disabled")
    elif pressed_button == 3:
        num_3.config(state="disabled")
    elif pressed_button == 4:
        num_4.config(state="disabled")
    elif pressed_button == 5:
        num_5.config(state="disabled")
    elif pressed_button == 6:
        num_6.config(state="disabled")
    elif pressed_button == 7:
        num_7.config(state="disabled")
    elif pressed_button == 8:
        num_8.config(state="disabled")
    elif pressed_button == 9:
        num_9.config(state="disabled")
    elif pressed_button == 10:
        num_10.config(state="disabled")
    else:
        pass


def winner_window():
    pass


win = tk.Tk()
win.title("Number Guessing Game")
win.geometry("250x400")

first_label = tk.Label(win, text="Guess a number between 1 and 10...")
first_label.pack()

start_game = tk.Button(win, text="Start Game", command=start_game)
start_game.pack()

num_1 = tk.Button(win, text="1", state="disabled", command=lambda: [n.guess_number(1),
                                                                    button_guess(1)])
num_1.pack()

num_2 = tk.Button(win, text="2", state="disabled", command=lambda: [n.guess_number(2),
                                                                    button_guess(2)])
num_2.pack()

num_3 = tk.Button(win, text="3", state="disabled", command=lambda: [n.guess_number(3),
                                                                    button_guess(3)])
num_3.pack()

num_4 = tk.Button(win, text="4", state="disabled", command=lambda: [n.guess_number(4),
                                                                    button_guess(4)])
num_4.pack()

num_5 = tk.Button(win, text="5", state="disabled", command=lambda: [n.guess_number(5),
                                                                    button_guess(5)])
num_5.pack()

num_6 = tk.Button(win, text="6", state="disabled", command=lambda: [n.guess_number(6),
                                                                    button_guess(6)])
num_6.pack()

num_7 = tk.Button(win, text="7", state="disabled", command=lambda: [n.guess_number(7),
                                                                    button_guess(7)])
num_7.pack()

num_8 = tk.Button(win, text="8", state="disabled", command=lambda: [n.guess_number(8),
                                                                    button_guess(8)])
num_8.pack()

num_9 = tk.Button(win, text="9", state="disabled", command=lambda: [n.guess_number(9),
                                                                    button_guess(9)])
num_9.pack()

num_10 = tk.Button(win, text="10", state="disabled", command=lambda: [n.guess_number(10),
                                                                      button_guess(10)])
num_10.pack()


exit_button = tk.Button(win, text='Exit', width=10, command=win.destroy)  # exit button closes window
exit_button.pack()


win.mainloop()
