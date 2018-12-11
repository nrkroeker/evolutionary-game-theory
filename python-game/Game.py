from World import World
from tkinter import *
import time

""" Class handling the construction of the necessary elements and the Tk window """
class Game(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.title("Game of Life")
        # Declare Tk variables to dynamically update labels
        self.gridSize = StringVar()
        self.generationLabel = StringVar()
        self.autoGenerating = False

        # Default grid size 25
        self.world = World(self, 25)
        self.world.grid(row=0, column=0)

        # Set initial grid values
        self.gridSize.set("25x25")
        self.generationLabel.set("0")
        self.world.generateCells()

        # Create all necessary buttons
        actions = Frame(self)
        actions.grid(row=1, column=0, pady=10)

        randomize = Button(actions, text="Randomize", command=self.randomizeGen)
        randomize.grid(row=0, column=0, padx=10)

        clear = Button(actions, text="Clear", command=self.clearGrid)
        clear.grid(row=0, column=1, padx=10)

        startGen = Button(actions, text="Start", command=self.startAutoGeneration)
        startGen.grid(row=0, column=2, padx=10)

        startGen = Button(actions, text="Stop", command=self.stopAutoGeneration)
        startGen.grid(row=0, column=3, padx=10)

        nextGen = Button(actions, text="Next Generation", command=self.nextGeneration)
        nextGen.grid(row=0, column=4, padx=10)

        gen = Label(actions, textvariable=self.generationLabel)
        gen.grid(row=0, column=5, padx=10)

        smaller = Button(actions, text="-", command=self.decreaseGrid)
        smaller.grid(row=0, column=6, ipadx=5, padx=10)

        bigger = Button(actions, text="+", command=self.increaseGrid)
        bigger.grid(row=0, column=7, ipadx=5, padx=10)

        size = Label(actions, textvariable=self.gridSize)
        size.grid(row=0, column=8)

        mainloop()
    
    # Method to update the label for grid size
    def updateSizeLabel(self):
        newSize = str(self.world.size)
        self.gridSize.set(newSize + "+" + newSize)

    # Method to increase the size of the grid
    def increaseGrid(self):
        self.world.updateSize(1)
        self.updateSizeLabel()

    # Method to decrease the size of the grid
    def decreaseGrid(self):
        self.world.updateSize(-1)
        self.updateSizeLabel()

    # Method to manually step to the next generation
    def nextGeneration(self):
        self.world.increaseGeneration()
        self.generationLabel.set(str(self.world.generation))

    # Method to initialize auto generation only if it isn't already running
    def startAutoGeneration(self):
        if (not self.autoGenerating):
            self.autoGenerating = True
            self.generation()

    # Recursive method to maintain auto generation
    def generation(self):
        self.nextGeneration()
        global game_running
        game_running = self.after(100, self.generation)
        
    # Method to cancel additional Tk function call and subsequent generation
    def stopAutoGeneration(self):
        self.after_cancel(game_running)
        self.autoGenerating = False

    # Method to set all cells in the grid to a random state
    def randomizeGen(self):
        self.world.generateCells()

    # Method to set all cells as dead
    def clearGrid(self):
        self.world.setCells(0)
        self.generationLabel.set(str(self.world.generation))