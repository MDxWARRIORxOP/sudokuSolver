from tkinter import *

root = Tk()  # create a new window

root.geometry("440x620")  # set the window size to 440 width and 620 height
root.title("Sudoku")  # set the window title to "Sudoku"
# set the background color to #36393E (which is also discord's dark theme color)
root.config(background="#36393E")

# creating a label at the top of the screen, to briefly explain the game
topLabel = Label(root,
                 text="Fill in the numbers below and click solve to solve the board, \n or click generate random to generate a random board then click solve to solve the board.",
                 foreground="white",
                 background="#36393E",
                 pady=10).grid(row=0, column=1, columnspan=10)

# creating a label which displays errors
invalidLabel = Label(root,
                     text="",
                     foreground="red",
                     background="#36393E").grid(row=15, column=1, columnspan=10, pady=5)

# creating a label which tells you if the board is solved
validLabel = Label(root,
                   text="",
                   foreground="green",
                   background="#36393E").grid(row=15, column=1, columnspan=10, pady=5)

# cells dict which we'll be using later on for drawing grids
cells = {}


def isNumber(P):
    # checking if the number entered is a valid int or not
    re = (P.isdigit() or P == "") and len(P) < 2
    return re


reg = root.register(isNumber)


def drawGrid3(row, column):  # drawing the 3x3 grid
    for r in range(3):  # r = row
        for c in range(3):  # c = column
            e = Entry(root,
                      width=1,
                      background="white",
                      justify="center",
                      validate="key",
                      validatecommand=(reg, "%P"))

            e.grid(row=row+r+1, column=column+c+1,
                   sticky="nsew", padx=1, pady=1, ipady=5)

            cells[(row+r+1, column+c+1)] = e


def drawGrid9():  # drawing the 9x9 grid
    for rn in range(1, 10, 3):  # rn = row number
        for cn in range(0, 9, 3):  # cn = column using
            drawGrid3(rn, cn)  # invoking draw grid function


def clearBoard():  # clearing the board
    # setting the invalid Label to an empty string
    invalidLabel.config(text="")
    validLabel.config(text="")  # setting the valid Label to an empty string

    for r in range(2, 11):  # r = row
        for c in range(1, 10):  # c = column
            cell = cells[(r, c)]
            cell.delete(0, "end")  # deleting stuff from cells dict


def getBoard():
    board = []

    # clearing the labels
    # setting the invalid Label to an empty string
    invalidLabel.config(text="")
    validLabel.config(text="")  # setting the valid Label to an empty string

    for r in range(2, 11):  # r = row
        rows = []
        for c in range(1, 10):  # c = column
            value = cells[(r, c)].get()

            if value == "":
                # setting the value as an empty space (0) if the value of cells[(r, c)] is == ""
                r.append(0)
            else:
                rows.append(int(value))  # else setting the int value of value

        board.append(rows)  # adding rows to the board


def generateRandomBoard():  # TODO: complete this function which generates a random board
    pass


def quitButtonFunction():
    root.destroy()
    quit()


solveButton = Button(root,
                     command=getBoard,
                     text="solve",
                     width=10)

solveButton.grid(row=20, column=1, columnspan=5, pady=20)

clearbutton = Button(root,
                     command=clearBoard,
                     text="clear",
                     width=10)

clearbutton.grid(row=20, column=5, columnspan=5, pady=20)

generateRandomButton = Button(root,
                              command=generateRandomBoard,
                              text="Generate",
                              width=10)

generateRandomButton.grid(row=30, column=1, columnspan=5, pady=20)

quitButton = Button(root,
                    command=quitButtonFunction,
                    text="quit",
                    width=10)

quitButton.grid(row=30, column=5, columnspan=5, pady=20)

drawGrid9()  # drawing the 9x9 grid

root.mainloop()  # open the window
