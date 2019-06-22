require_relative 'player'

class Game
    attr_reader :players, :name
    def initialize(name='The Game')
        @name = name
        @players = []
    end
    def add_player(p)
        @players.push(p)
    end
    def play 
        puts "There are #{players.size} players in the game."
        players.each do |player|
            puts player
            #player.healthReport
        end
    end
end