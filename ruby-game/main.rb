require 'Qt'


class QtApp < Qt::Widget

    def initialize
        super
        
        setWindowTitle "Tooltip"

        setToolTip "This is Qt::Widget"
        
        resize 250, 150
        move 300, 300

        show
    end
end

app = Qt::Application.new ARGV
QtApp.new
app.exec