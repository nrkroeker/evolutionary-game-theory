from World import World
from tkinter import *

class Game:
    gridWidth = 2
    gridHeight = 2

    def __init__(self):
        self.tk = Tk()
        canvas = Canvas(self.tk, width=502, height=502, bg="white", bd=2, highlightthickness=0, relief="groove")
        canvas.grid(row=0, column=0, pady=20, padx=50)
        
        
        self.world = World(2, 2)
        self.world.generateCells()
        for cell in self.world.cells:
            if cell.state == 0:
                fill = "black"
            else:
                fill = "white"
            canvas.create_rectangle(cell.xIndex * 250, cell.yIndex * 250, cell.xIndex * 250 + 250, cell.yIndex * 250 + 250,  fill=fill)


        # canvas.create_line(0, 0, 0, 500) # top-left to bottom-left
        # canvas.create_line(0, 0, 500, 0) # top-left to top-right
        # canvas.create_line(0, 500, 500, 500) # bottom-left to bottom-right
        # canvas.create_line(500, 0, 500, 500) # top-right to bottom-right
        canvas.create_line(0, 250, 500, 250) # grid lines
        canvas.create_line(250, 0, 250, 500) # grid lines
        # canvas.create_rectangle()
        actions = Frame(self.tk)
        actions.grid(row=1, column=0)

        start = Button(actions, text="Next Generation")
        start.grid(row=0, column=0)

        mainloop()

    # def renderCells(self):

