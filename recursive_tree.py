from tkinter import *
import random

SIZE = 800

count = 0


def create_window():
    global root
    root = Tk()
    root.geometry(f"{SIZE}x{SIZE}")
    #root.resizable(height=False, width=False)
    root.config(bg="#F1ECC3")
    root.title("the recursive tree")

    global canvas
    canvas = Canvas(width=SIZE, height=SIZE,
                    bg="#F1ECC3", highlightthickness=0)
    canvas.pack()
    random.seed()


def tree(length, x, y):
    global count
    len1 = random.randint(55, 99)
    len2 = random.randint(55, 99)
    rand1x = random.randint(1, 3)
    rand2x = random.randint(1, 3)
    rand1y = random.randint(1, 5)
    rand2y = random.randint(1, 5)

    if length >= 4:
        tree(length*len1/100, x+rand1x*length,  y-rand1y*length)
        tree(length*len2/100, x-rand2x*length,  y-rand2y*length)
    t1 = canvas.create_line(x, y, x+rand1x*length, y-rand1y*length)
    t1 = canvas.create_line(x, y, x-rand2x*length, y-rand2y*length)


#########################################


create_window()

canvas.create_line(SIZE//2, SIZE, SIZE//2, SIZE-100)
tree(50, SIZE//2, SIZE-100)

root.mainloop()
