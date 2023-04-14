from NumberGuesser_class import NumberGuesser
import tkinter as tk


def start_game():
    n = NumberGuesser()


# def display_text(text):
    # tk.Label(win, text=text).grid(row=14)


# def win_prompt():
    # tk.messagebox.showinfo("Winner", "You selected the correct number!")

win = tk.Tk()
win.title("Number Guessing Game")
win.geometry("250x400")

first_label = tk.Label(win, text="Guess a number between 1 and 10...")
first_label.pack()

start_game = tk.Button(win, text="Start Game", command=start_game)
start_game.pack()

num_1 = tk.Button(win, text="1", command=lambda: [n.guess_number(1),
                                                  n.add_number(1)])
num_1.pack()

num_2 = tk.Button(win, text="2", command=lambda: [n.guess_number(2),
                                                  n.add_number(2)])
num_2.pack()

num_3 = tk.Button(win, text="3", command=lambda: [n.guess_number(3),
                                                  n.add_number(3)])
num_3.pack()

num_4 = tk.Button(win, text="4", command=lambda: [n.guess_number(4),
                                                  n.add_number(4)])
num_4.pack()

num_5 = tk.Button(win, text="5", command=lambda: [n.guess_number(5),
                                                  n.add_number(5)]).grid(row=6)

num_6 = tk.Button(win, text="6", command=lambda: [n.guess_number(7),
                                                  n.add_number(7)]).grid(row=7)

num_7 = tk.Button(win, text="7", command=lambda: [n.guess_number(8),
                                                  n.add_number(8)]).grid(row=8)

num_8 = tk.Button(win, text="8", command=lambda: [n.guess_number(8),
                                                  n.add_number(8)]).grid(row=9)

num_9 = tk.Button(win, text="9", command=lambda: [n.guess_number(9),
                                                  n.add_number(9)]).grid(row=10)

num_10 = tk.Button(win, text="10", command=lambda: [n.guess_number(10),
                                                    n.add_number(10)]).grid(row=11)


# reset_button = tk.Button(text="Reset", command=reset_game)
# reset_button.grid(row=5)

exit_button = tk.Button(win, text='Exit', width=10, command=win.destroy)  # exit button closes window
exit_button.grid(row=12)

# btn1 = tk.Button(tk, text="1", command=lambda: print_text("Button 1"))
