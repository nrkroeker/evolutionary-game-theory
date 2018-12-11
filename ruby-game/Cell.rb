require "tk"

# Class handling the internal state of a given cell
class Cell
    def initialize(xIndex, yIndex, state, canvas, cellSize)
        @state = state
        @xIndex = xIndex
        @yIndex = yIndex
        @canvas = canvas
        @cellSize = cellSize
        
        # Set initial fill/outline values
        getColor
        x1 = @xIndex * @cellSize
        y1 = @yIndex * @cellSize
        x2 = @xIndex * @cellSize + @cellSize
        y2 = @yIndex * @cellSize + @cellSize
        
        # Generate actual Tk rectangle element and bind click listener
        @element = TkcRectangle.new(canvas, x1, y1, x2, y2, 'fill'=>@fill, 'outline'=>@outline)
        p = proc { toggleState }
        @element.bind("1", p)
    end

    # Method to return the cell's state
    def state
        @state
    end

    # Method to set a cell's state value and trigger color update
    def setState(state)
        @state = state
        getColor
        @element.configure('fill', @fill)
        @element.configure('outline', @outline)
    end

    # Method to set a cell's state to the opposite of its current state
    def toggleState()
        @state = @state == 0 ? 1 : 0
        getColor
        @element.configure('fill', @fill)
        @element.configure('outline', @outline)
    end
    
    # Method to set color variables for the cell's current state
    def getColor
        if @state == 0
            @fill = "white"
            @outline = "black"
        else
            @fill = "black"
            @outline = "white"
        end
    end
end