class Player
    attr_accessor :name
    attr_reader :health
    def score
        @name.length + @health
    end

    def initialize(name,health=100)
        @name = name.capitalize
        @health = health
    end
    def to_s
        "I'm #{@name} with a health of #{@health} and a score of #{score}"
    end
    def blam
        puts "#{@name} got blammed"
        @health -= 10
    end
    def w00t
        puts "#{@name} got w00ted"
        @health += 15
    end
    def healthReport
        blam 
        w00t 
        blam 
    end
    def strong?
        if @health > 100
            return true
        else
            return false
        end
    end
end

if __FILE__ == $0
    player = Player.new("moe")
    puts player.name
    puts player.health
    player.w00t
    puts player.health
    player.blam
    puts player.health
    puts player.score
  end