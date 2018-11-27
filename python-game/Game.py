from World import World
from tkinter import *

class Game(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.title("Game of Life")
        self.gridSize = StringVar()
        self.generation = StringVar()
        
        self.world = World(self, 25)
        self.world.grid(row=0, column=0, pady=20, padx=50)

        self.gridSize.set("25x25")
        self.generation.set("0")
        self.world.generateCells()

        actions = Frame(self)
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

    def updateSizeLabel(self):
        newSize = str(self.world.size)
        self.gridSize.set(newSize + "+" + newSize)

    def increaseGrid(self):
        self.world.updateSize(1)
        self.updateSizeLabel()

    def decreaseGrid(self):
        self.world.updateSize(-1)
        self.updateSizeLabel()

    def nextGeneration(self):
        print("increasing generation")
        self.world.increaseGeneration()
        self.generation.set(str(self.world.generation))
        print("generation increased")


