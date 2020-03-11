import tkinter as tk
import random

root = tk.Tk()
root.title('Guessing Game') # add title to gui
image=tk.PhotoImage(file="PGIPLogo.png") # load an image
lable_image =tk.Label(image=image)
lable_image.pack()
canvas1 = tk.Canvas(root, width=400, height=300) # create window
canvas1.pack()
# add Title to window
title=tk.Label(root, text='From 1-10, can you guess what number I am thinking?', bg="light blue", fg="black", font=('helvetica', 12))
canvas1.create_window(200, 25, window=title)
label2=tk.Label(root, text='Enter your number. Good Luck', font=('helvetica', 10)) # add instructions
canvas1.create_window(200, 75, window=label2)
user_input = tk.Entry(root) # ask user input
canvas1.create_window(200, 140, window=user_input)
number =random.randrange(1,10)
def game():
    try:
        guess = int(user_input.get())
        if guess == number:
            message = "You are correct!"
        elif guess < number:
            message = "Your guess is too low. "
        elif guess > number:
            message = "Your guess is too high."
    except ValueError:
        message = "Your guess needs to be a number."
    results = tk.Label(root, text=message, width=40)
    canvas1.create_window(200, 230, window=results)

button1 = tk.Button(text='Guess', command=game)
canvas1.create_window(200, 180, window=button1)

root.mainloop()