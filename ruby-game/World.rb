require 'tk'
require_relative 'Cell'

class World
    def initialize(size, root)
        @generation = 0
        @canvasSize = 650
        @cells = []
        @size = size
        @root = root

        # Generate initial canvas
        @canvas = TkCanvas.new(@root, :height => 650, :width => 650)
    end

    # Method to return the canvas to be gridded
    def canvas
        @canvas
    end

    # Method to return the current generation number
    def generation
        @generation
    end

    # Method to return the current world/grid size in squares
    def size
        @size
    end
    
    # Method to alter grid size by a given increment, positive or negative
    def updateSize(increment)
        @size += increment
        generateCells
    end

    # Method to generate cells on the canvas
    def generateCells
        @canvas.delete('all')

        # Size of a given cell in pixels
        cellSize = @canvasSize / @size

        @cells = []
        @size.times do |x|
            @cells.push []
            @size.times do |y|
                tempState = rand(3)
                # Simple check to increase the probability that a cell starts dead
                if (tempState == 2 || tempState == 3)
                    tempState = 0
                end
                c = Cell.new(x, y, tempState, @canvas, cellSize)
                @cells[x].push c
                # end
            end
        end
    end

    # Method to set all cells to a given state
    def setCells(state)
        @generation = 0
        @size.times do |x|
            @size.times do |y|
                @cells[x][y].setState(state)
            end
        end
    end

    # Method to reset the generation number back to 0
    def resetGeneration
        @generation = 0
    end
    
    # Method to determine the number of live cells adjacent to a given cell
    def checkCell(i, j)
        s = 0 # Count of live adjacent cells
        for x in [i-1, i, i+1] do
            for y in [j-1, j, j+1] do
                if (x == i && y == j)
                    next # Skip the current point
                end
                if (x != @size && y != @size)
                    s += @cells[x][y].state
                # If adjacent cells are off the grid, loop around to other size
                elsif (x == @size && y != @size)
                    s += @cells[0][y].state
                elsif (x != @size && y == @size)
                    s += @cells[x][0].state
                else
                    s += @cells[0][0].state
                end
            end
        end
        return s
    end      
  
    # Method to increase the generation and check all cell states
    def increaseGeneration
        @generation += 1
        @size.times do |x|
            @size.times do |y|
                cell = @cells[x][y]
                # Get count of live neighbors
                n = checkCell(x, y)
                if (cell.state == 0 && n == 3)
                    cell.toggleState
                elsif (cell.state == 1 && n != 2 && n != 3)
                    cell.toggleState
                end
            end
        end
    end

end