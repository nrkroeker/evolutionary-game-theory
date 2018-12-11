require_relative "World"
require "tk"

# Class handling the construction of the necessary elements and the Tk window
class Game
    # Method to update the size label with correct formatting, e.g. 25x25
    def updateSizeLabel
        @sizeText.value = "#{@world.size}x#{@world.size}"
    end
    
    # Method to increase the size of the grid
    def increaseGrid
        @world.updateSize(1)
        updateSizeLabel
    end
    
    # Method to decrease the size of the grid
    def decreaseGrid
        @world.updateSize(-1)
        updateSizeLabel
    end
    
    # Method to step to the next generation manually
    def nextGeneration
        @world.increaseGeneration
        @genText.value = @world.generation
    end
    
    # Method to initialize auto generation, only if it hasn't already started
    def startAutoGeneration
        if (not @autoGenerating)
            @autoGenerating = true
            generation
        end
    end
    
    # Recursive method for auto generation
    def generation
        nextGeneration
        @game_running = @root.after(100) { generation }
    end
        
    # Method to stop auto generation by cancelling the function call
    def stopAutoGeneration
        @root.after_cancel(@game_running)
        @autoGenerating = false
    end
    
    # Method to set all cells to a random state
    def randomGen
        @world.generateCells
        @world.resetGeneration
        @genText.value = @world.generation
    end

    # Method to clear all cells back to dead state
    def clearGrid
        @world.setCells(0)
        @world.resetGeneration
        @genText.value = @world.generation
    end

    def initialize
        @autoGenerating = false

        @root = TkRoot.new do
            title "Game of life"
        end

        # Default grid size 25
        @world = World.new(25, @root)
        @world.canvas.grid(:row=>0, :column=>0)

        # Declare TkVariable properties for dynamic labels
        @sizeText = TkVariable.new
        @sizeText.value = "25 x 25"
        @genText = TkVariable.new
        @genText.value = "0"
        @world.generateCells

        # Create all necessary buttons
        @actions = TkFrame.new {
            grid(:row=>1, :column=>0, :pady=>10)
        }

        reset = proc { clearGrid }
        @resetButton = Tk::Tile::Button.new(@actions) {
            text "Clear"
            command reset
            grid(:row=>0, :column=>0, :padx=>10)
        }

        random = proc { randomGen }
        @randomButton = Tk::Tile::Button.new(@actions) {
            text "Random"
            command random
            grid(:row=>0, :column=>1, :padx=>10)
        }

        start = proc { startAutoGeneration }
        @startGenButton = Tk::Tile::Button.new(@actions) {
            text "Start"
            command start
            grid(:row=>0, :column=>2, :padx=>10)
        }

        stop = proc { stopAutoGeneration }
        @stopGenButton= Tk::Tile::Button.new(@actions) {
            text "Stop"
            command stop
            grid(:row=>0, :column=>3, :padx=>10)
        }

        nextGen = proc { nextGeneration }
        @nextGenButton = Tk::Tile::Button.new(@actions) {
            text "Next Generation"
            command nextGen
            grid(:row=>0, :column=>4, :padx=>10)
        }

        @genLabel = Tk::Tile::Label.new(@actions) {
            textvariable
            grid(:row=>0, :column=>5, :padx=>10)
        }
        @genLabel["textvariable"] = @genText

        reduce = proc { decreaseGrid }
        @reduceButton = Tk::Tile::Button.new(@actions) {
            text "-"
            command reduce
            grid(:row=>0, :column=>6, :ipadx=>5, :padx=>10)
        }

        increase = proc {increaseGrid}
        @increaseButton = Tk::Tile::Button.new(@actions) {
            text "+"
            command increase
            grid(:row=>0, :column=>7, :ipadx=>5, :padx=>10)
        }

        @sizeLabel = Tk::Tile::Label.new(@actions) {
            textvariable
            grid(:row=>0, :column=>8)
        }
        @sizeLabel["textvariable"] = @sizeText

        @root.mainloop
    end
    
end