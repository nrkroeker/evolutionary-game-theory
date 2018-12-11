import random
from tkinter import *
from Cell import Cell

class World(Frame):
    size = 0
    canvasSize = 650
    generation = 0

    def __init__(self, parent, size):
        Frame.__init__(self, parent, bg="red")
        self.parent = parent
        self.cells = []
        self.size = size

        # Create initial canvas for cell rendering
        self.canvas = Canvas(self, width=self.canvasSize, height=self.canvasSize, bg="white", highlightthickness=0, relief="groove")
        self.canvas.grid(row=0, column=0)

    # Method to change the size by some increment, positive or negative
    def updateSize(self, increment):
        self.size += increment
        self.generateCells()

    # Regenerate all cells on the canvas
    def generateCells(self):
        self.canvas.delete("all")

        # How wide/tall in pixels the cell needs to be
        cellSize = self.canvasSize / self.size

        self.cells = []
        for x in range(0, self.size):
            row = []
            for y in range(0, self.size):
                tempState = random.randint(0, 3)
                # Simple check to increase the probability that a cell starts dead
                if (tempState == 2 or tempState == 3):
                    tempState = 0
                row.append(Cell(x, y, tempState, self.canvas, cellSize))
            self.cells.append(row)

    # Iterate over cells and set all states to the given value
    def setCells(self, state):
        self.generation = 0
        for x in range(0, self.size):
            for y in range(0, self.size):
                self.cells[x][y].setState(state)

    # Set generation value back to 0
    def resetGeneration(self):
        self.generation = 0

    # Increase generation manually by one step
    def increaseGeneration(self):
        self.generation += 1
        for x in range(0, self.size):
            for y in range(0, self.size):
                cell = self.cells[x][y]
                n = self.checkCell(x, y)
                if (cell.state == 0 and n == 3):
                    cell.toggleState()
                elif (cell.state == 1 and n != 2 and n != 3):
                    cell.toggleState()

    # Determine the number of live cells adjacent to a given cell
    def checkCell(self, i, j):
        s = 0 # Count of live adjacent cells
        for x in [i-1, i, i+1]:
            for y in [j-1, j, j+1]:
                # Skip the current point
                if(x == i and y == j):
                    continue
                if (x != self.size and y != self.size):
                    s += self.cells[x][y].state
                # If adjacent cells are off the grid, loop around to other size
                elif (x == self.size and y != self.size):
                    s += self.cells[0][y].state
                elif (x != self.size and y == self.size):
                    s += self.cells[x][0].state
                else:
                    s += self.cells[0][0].state
        return s

        
