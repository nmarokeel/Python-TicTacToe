# Naramsin Marokeel, CIS345, 12pm, A7

# importing tkinter to use for the GUI
from tkinter import *
from tkinter import messagebox

# creating the gui and setting it's name and geometry size, as well as packing it in a frame
tk = Tk()
tk.title('Tic Tac Toe')
tk.geometry('300x255')


def btn_click(button):
    """Button Click, used for when the gui is started, the first button clicked is player 1 which is X and then the
    second button is clicked which is Player 2, O"""
    global counter, buttonClick
    if button["text"] == " " and buttonClick == True:
        button["text"] = 'X'
        button.configure(state=DISABLED)
        buttonClick = False
        check_win(button)
        counter += 1

    elif button["text"] == " " and buttonClick == False:
        button["text"] = "O"
        button.configure(state=DISABLED)
        buttonClick = True
        check_win(button)
        counter += 1


def enable_btn():
    """Enables the buttons so the game can start again"""
    btn_one.config(state=NORMAL)
    btn_two.config(state=NORMAL)
    btn_three.config(state=NORMAL)
    btn_four.config(state=NORMAL)
    btn_five.config(state=NORMAL)
    btn_six.config(state=NORMAL)
    btn_seven.config(state=NORMAL)
    btn_eight.config(state=NORMAL)
    btn_nine.config(state=NORMAL)


def clear_board():
    """Resets the text variable back to a blank string so player one can start a new game"""
    btn_one.configure(text=" ")
    btn_two.configure(text=" ")
    btn_three.configure(text=" ")
    btn_four.configure(text=" ")
    btn_five.configure(text=" ")
    btn_six.configure(text=" ")
    btn_seven.configure(text=" ")
    btn_eight.configure(text=" ")
    btn_nine.configure(text=" ")


def check_win(button):
    """Check_win: used for when the players are choosing their spots. If the spots mark three in a row, the player then
    wins the game and a pop up appears saying that the player won."""
    global counter, buttonClick
    if (btn_one['text'] == 'X' and btn_two['text'] == 'X' and btn_three['text'] == 'X' or
            btn_four['text'] == 'X' and btn_five['text'] == 'X' and btn_six['text'] == 'X' or
            btn_seven['text'] == 'X' and btn_eight['text'] == 'X' and btn_nine['text'] == 'X' or
            btn_one['text'] == 'X' and btn_five['text'] == 'X' and btn_nine['text'] == 'X' or
            btn_one['text'] == 'X' and btn_four['text'] == 'X' and btn_seven['text'] == 'X' or
            btn_three['text'] == 'X' and btn_five['text'] == 'X' and btn_seven['text'] == 'X' or
            btn_two['text'] == 'X' and btn_five['text'] == 'X' and btn_eight['text'] == 'X' or
            btn_three['text'] == 'X' and btn_six['text'] == 'X' and btn_nine['text'] == 'X'):
        messagebox.showinfo('Tic Tac Toe', "Player 1 is the Winner!!")
        clear_board()
        enable_btn()
        counter=0
        buttonClick= True

    elif counter == 9:
        messagebox.showinfo('Tic Tac Toe', "Cats Game")
        clear_board()
        enable_btn()
        counter = 0
        buttonClick = True

    elif (btn_one['text'] == 'O' and btn_two['text'] == 'O' and btn_three['text'] == 'O' or
          btn_four['text'] == 'O' and btn_five['text'] == 'O' and btn_six['text'] == 'O' or
          btn_seven['text'] == 'O' and btn_eight['text'] == 'O' and btn_nine['text'] == 'O' or
          btn_one['text'] == 'O' and btn_five['text'] == 'O' and btn_nine['text'] == 'O' or
          btn_one['text'] == 'O' and btn_four['text'] == 'O' and btn_seven['text'] == 'O' or
          btn_three['text'] == 'O' and btn_five['text'] == 'O' and btn_seven['text'] == 'O' or
          btn_two['text'] == 'O' and btn_five['text'] == 'O' and btn_eight['text'] == 'O' or
          btn_three['text'] == 'O' and btn_six['text'] == 'O' and btn_nine['text'] == 'O'):
        messagebox.showinfo('Tic Tac Toe', "Player 2 is the Winner!!")
        clear_board()
        enable_btn()
        counter=0
        buttonClick = True


# Creating variables to be used for the event handlers above
buttonClick = True
# counter is the number of button clicks there has been
counter = 0

# Creating the buttons for the user to click on
btn_one = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_one))
btn_two = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_two))
btn_three = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_three))

# placing the buttons in the frame labeld tk
btn_one.grid(row=0, column=0)
btn_two.grid(row=0, column=1)
btn_three.grid(row=0, column=2)

# Creating buttons
btn_four = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_four))
btn_five = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_five))
btn_six = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_six))

# placing the buttons
btn_four.grid(row=1, column=0)
btn_five.grid(row=1, column=1)
btn_six.grid(row=1, column=2)

# creating the buttons
btn_seven = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_seven))
btn_eight = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_eight))
btn_nine = Button(tk, text=" ", width=13, height=5, command=lambda: btn_click(btn_nine))

# placing the buttons
btn_seven.grid(row=2, column=0)
btn_eight.grid(row=2, column=1)
btn_nine.grid(row=2, column=2)

# used to keep the gui opened
tk.mainloop()

