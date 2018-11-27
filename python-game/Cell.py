class Cell:
    state = 0 # 0 is dead, 1 is alive

    def __init__(self, xIndex, yIndex, state):
        self.state = state
        self.xIndex = xIndex
        self.yIndex = yIndex

    def toggleState(self):
        self.state = self.state == 0 ? 1 : 0

    # def getSiblings(self):
        