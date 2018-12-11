from tkinter import *

""" Class handling the internal state of a given cell """
class Cell(Frame):
    state = 0 # 0 is dead, 1 is alive

    def __init__(self, xIndex, yIndex, state, canvas, cellSize):
        self.state = state
        self.xIndex = xIndex
        self.yIndex = yIndex
        self.canvas = canvas

        cellColor = self.getColor()
        # Create a rectangle on the canvas representing the cell
        self.element = self.canvas.create_rectangle(self.xIndex * cellSize, self.yIndex * cellSize, self.xIndex * cellSize + cellSize, self.yIndex * cellSize + cellSize, fill=cellColor["fill"], outline=cellColor["outline"])
        self.canvas.tag_bind(self.element, "<Button-1>", self.handleClick)

    # Handler for click event
    def handleClick(self, event):
        self.toggleState()

    # Method to toggle a cell from alive to dead or vice versa, and update color
    def toggleState(self):
        self.state = 1 if self.state == 0 else 0
        cellColor = self.getColor()
        self.canvas.itemconfigure(self.element, fill=cellColor["fill"], outline=cellColor["outline"])

    # Method to set a cell's state to a specific value
    def setState(self, state):
        self.state = state
        cellColor = self.getColor()
        self.canvas.itemconfigure(self.element, fill=cellColor["fill"], outline=cellColor["outline"])

    # Method to determine the fill/outline colors of the cell
    def getColor(self):
        if self.state == 0:
            fill = "white"
            outline = "black"
        else:
            fill = "black"
            outline = "white"
        return {
            "fill": fill,
            "outline": outline
        }
