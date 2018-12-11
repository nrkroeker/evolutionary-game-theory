require "tk"

# Class handling the internal state of a given cell
class Cell
    def initialize(xIndex, yIndex, state, canvas, cellSize)
        @state = state
        @xIndex = xIndex
        @yIndex = yIndex
        @canvas = canvas
        @cellSize = cellSize
        
        getColor
        x1 = @xIndex * @cellSize
        y1 = @yIndex * @cellSize
        x2 = @xIndex * @cellSize + @cellSize
        y2 = @yIndex * @cellSize + @cellSize
        
        @element = TkcRectangle.new(canvas, x1, y1, x2, y2, 'fill'=>@fill, 'outline'=>@outline)
        p = proc { toggleState }
        @element.bind("1", p)
    end

    def state
        @state
    end

    def setState(state)
        @state = state
        getColor
        @element.configure('fill', @fill)
        @element.configure('outline', @outline)
    end

    def toggleState()
        @state = @state == 0 ? 1 : 0
        getColor
        @element.configure('fill', @fill)
        @element.configure('outline', @outline)
    end

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