class Practice
    attr_accessor :myArray
    attr_reader :name
    attr_writer :modifier
    
    def initialize(newname="Something",newmodifier = 1) 
        #puts "something"
        @name = newname
        @modifier = newmodifier
        @myArray = []
    end

    def to_s
        "Practice name: #{@name}\n Modifier at: #{@modifier}"
    end
    def modifierStatus
        @modifier
    end
    def modifierIsOne
        if @modifier == 1
            return "One"
        else
            return "More"
        end
    end
end
