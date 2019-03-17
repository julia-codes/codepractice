my_favorite_movie = "Goonies"
your_favorite_movie = my_favorite_movie
puts your_favorite_movie

my_favorite_movie[0] = 'L'
puts "#{your_favorite_movie} is Loonies"

my_favorite_movie = "Ghostbusters"
puts "#{your_favorite_movie} is Loonies"

puts "ri for documentation"
puts ""

puts "predicate methods end in a ?"
my_favorite_movie.start_with?("G")

puts "method with ! does it in place on that object"

my_favorite_movie = "ghostbusters"
title = my_favorite_movie.capitalize.ljust(30, '.')
puts title

puts self
puts self.class
puts "private methods can't have a reciever (?)"
