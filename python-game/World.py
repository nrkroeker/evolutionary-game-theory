from Cell import Cell
import random

class World:
    generation = 0
    width = 2
    height = 2

    def __init__(self, width, height):
        self.cells = []
        self.width = self.width
        self.height = self.height
    
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height

    def generateCells(self):
        self.cells = []
        for x in range(0, self.width):
            for y in range(0, self.height):
                state = random.randint(0, 1)
                self.cells.append(Cell(x, y, state))

    def resetGeneration(self):
        self.generation = 0

    def increaseGeneration(self):
        self.generation += 1
    
    # def checkCellStates(self):
        #iterate over cells and check state
        
