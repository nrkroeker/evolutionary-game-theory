from Cell import Cell
import random

class World:
    generation = 0
    size = 0

    def __init__(self, size):
        self.cells = []
        self.size = size
    
    def updateSize(self, increment):
        self.size += increment

    def generateCells(self):
        self.cells = []
        for x in range(0, self.size):
            for y in range(0, self.size):
                state = random.randint(0, 1)
                self.cells.append(Cell(x, y, state))

    def resetGeneration(self):
        self.generation = 0

    def increaseGeneration(self):
        self.generation += 1
        for x in range(0, self.size):
            for y in range(0, self.size):
                cell = self.cells[x][y]
                n = self.checkCell(x, y)
                if (cell.state == 0 && n == 3):
                    cell.toggleState()
                elif (cell.state == 1 && n != 2 && n != 3):
                    cell.toggleState()

    """ Determine the number of live cells adjacent to a given cell """
    def checkCell(self, i, j):
        s = 0 # Count of live adjacent cells
        for x in [i-1, i, i+1]:
            for y in [j-1, j, j+1]:
                if(x == i and y == j):
                    continue # Skip the current point
                if(x != self.size and y != self.size):
                    s += self.cells[x][y]
                # If adjacent cells are off the grid, loop around to other size
                elif(x == self.size and y != self.size):
                    s += self.cells[0][y]
                elif(x != self.size and y == self.size):
                    s += self.cells[x][0]
                else:
                    s += self.cells[0][0]
        return s

        
