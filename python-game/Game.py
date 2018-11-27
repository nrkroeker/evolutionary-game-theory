from World import World
from tkinter import *

class Game:
    canvasSize = 650

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Game of Life")
        self.gridSize = StringVar()
        self.generation = StringVar()

        self.canvas = Canvas(self.tk, width=self.canvasSize, height=self.canvasSize, bg="white", highlightthickness=0, relief="groove")
        self.canvas.grid(row=0, column=0, pady=20, padx=50)
        
        self.world = World(25)
        self.gridSize.set("25x25")
        self.generation.set("0")
        self.buildCells()

        actions = Frame(self.tk)
        actions.grid(row=1, column=0)

        start = Button(actions, text="Next Generation", command=self.nextGeneration)
        start.grid(row=0, column=0, padx=10)

        gen = Label(actions, textvariable=self.generation)

        smaller = Button(actions, text="-", command=self.decreaseGrid)
        smaller.grid(row=0, column=1, ipadx=5, padx=10)

        bigger = Button(actions, text="+", command=self.increaseGrid)
        bigger.grid(row=0, column=2, ipadx=5, padx=10)

        size = Label(actions, textvariable=self.gridSize)
        size.grid(row=0, column=3)

        mainloop()

    def buildCells(self):
        self.canvas.delete("all")
        self.world.generateCells()
        cellSize = self.canvasSize / self.world.size 

        for cell in self.world.cells:
            if cell.state == 0:
                fill = "black"
                outline = "white"
            else:
                fill = "white"
                outline = "black"
            self.canvas.create_rectangle(cell.xIndex * cellSize, cell.yIndex * cellSize, cell.xIndex * cellSize + cellSize, cell.yIndex * cellSize + cellSize, fill=fill, outline=outline)

    def updateSizeLabel(self):
        newSize = str(self.world.size)
        self.gridSize.set(newSize + "+" + newSize)

    def increaseGrid(self):
        self.world.updateSize(1)
        self.updateSizeLabel()
        self.buildCells()

    def decreaseGrid(self):
        self.world.updateSize(-1)
        self.updateSizeLabel()
        self.buildCells()

    def nextGeneration(self):
        self.generation.set(str(self.world.generation))
        self.world.increaseGeneration()


