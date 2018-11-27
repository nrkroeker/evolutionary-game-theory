from tkinter import *

class Cell(Frame):
    state = 0 # 0 is dead, 1 is alive

    def __init__(self, xIndex, yIndex, state, canvas, cellSize):
        self.state = state
        self.xIndex = xIndex
        self.yIndex = yIndex
        self.canvas = canvas

        cellColor = self.getColor()

        self.element = self.canvas.create_rectangle(self.xIndex * cellSize, self.yIndex * cellSize, self.xIndex * cellSize + cellSize, self.yIndex * cellSize + cellSize, fill=cellColor["fill"], outline=cellColor["outline"])

    def toggleState(self):
        self.state = 1 if self.state == 0 else 0
        cellColor = self.getColor()
        self.canvas.itemconfigure(self.element, fill=cellColor["fill"], outline=cellColor["outline"])

    def getColor(self):
        if self.state == 0:
            fill = "black"
            outline = "white"
        else:
            fill = "white"
            outline = "black"
        return {
            "fill": fill,
            "outline": outline
        }


    # def getSiblings(self):
        