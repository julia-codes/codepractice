class Movie

    def initialize(title,rank=0)
        @title = title.capitalize
        @rank = rank
    end  
    def to_s
        "#{@title} has a rank of #{@rank}" 
    end
    def thumbs_up
        @rank += 1
    end
    def thumbs_down
        @rank -= 1
    end
end

movie1 = Movie.new("goonies",10)
movie2 = Movie.new("ghostbusters",9)
movie3 = Movie.new("goldfinger")


movie1.thumbs_down
movie2.thumbs_up
puts movie1
puts movie2
puts movie3
