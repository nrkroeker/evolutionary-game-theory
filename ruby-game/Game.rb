require_relative "World"
require "tk"

# Class handling the construction of the necessary elements and the Tk window
class Game
    def updateSizeLabel
        @sizeText.value = "#{@world.size}x#{@world.size}"
    end
    
    def increaseGrid
        @world.updateSize(1)
        updateSizeLabel
    end
    
    def decreaseGrid
        @world.updateSize(-1)
        updateSizeLabel
    end
    
    def nextGeneration
        @world.increaseGeneration
        @genText = @world.generation
    end
    
    def startAutoGeneration
        if (not @autoGenerating)
            @autoGenerating = true
            generation
        end
    end
    
    def generation
        nextGeneration
        @game_running = @root.after(100) { generation }
    end
        
    def stopAutoGeneration
        @root.after_cancel(@game_running)
        @autoGenerating = false
    end
    
    def randomGen
        @world.generateCells
    end

    def clearGrid
        @world.setCells(0)
    end

    def initialize
        @autoGenerating = false

        @root = TkRoot.new do
            title "Game of life"
        end

        # Default grid size 25
        @world = World.new(25, @root)
        @world.canvas.grid(:row=>0, :column=>0)

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