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
    attr_accessor :title
    attr_reader :rank
end