from World import World
from tkinter import *
import time

""" Class handling the construction of the necessary elements and the Tk window """
class Game(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.title("Game of Life")
        self.gridSize = StringVar()
        self.generationLabel = StringVar()
        self.autoGenerating = False

        # Default grid size 25
        self.world = World(self, 25)
        self.world.grid(row=0, column=0, pady=20, padx=50)

        self.gridSize.set("25x25")
        self.generationLabel.set("0")
        self.world.generateCells()

        # Create all necessary buttons
        actions = Frame(self)
        actions.grid(row=1, column=0, pady=10)

        reset = Button(actions, text="Reset", command=self.resetGen)
        reset.grid(row=0, column=0, padx=10)

        startGen = Button(actions, text="Start", command=self.startAutoGeneration)
        startGen.grid(row=0, column=1, padx=10)

        startGen = Button(actions, text="Stop", command=self.stopAutoGeneration)
        startGen.grid(row=0, column=2, padx=10)

        nextGen = Button(actions, text="Next Generation", command=self.nextGeneration)
        nextGen.grid(row=0, column=3, padx=10)

        gen = Label(actions, textvariable=self.generationLabel)
        gen.grid(row=0, column=4, padx=10)

        smaller = Button(actions, text="-", command=self.decreaseGrid)
        smaller.grid(row=0, column=5, ipadx=5, padx=10)

        bigger = Button(actions, text="+", command=self.increaseGrid)
        bigger.grid(row=0, column=6, ipadx=5, padx=10)

        size = Label(actions, textvariable=self.gridSize)
        size.grid(row=0, column=7)

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
        self.world.increaseGeneration()
        self.generationLabel.set(str(self.world.generation))

    def startAutoGeneration(self):
        if (not self.autoGenerating):
            self.autoGenerating = True
            self.generation()

    def generation(self):
        self.nextGeneration()
        global game_running
        game_running = self.after(5, self.generation)
        
    def stopAutoGeneration(self):
        self.after_cancel(game_running)
        self.autoGenerating = False

    def resetGen(self):
        self.world.generateCells()