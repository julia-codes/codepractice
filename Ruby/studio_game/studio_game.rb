greeting = "Welcome!"

3.times do
    puts greeting
end
puts Time.now.strftime("Game starts at %m/%d/%Y ( %I:%M%P )")

def printHealth(player, health)
    "#{player.capitalize}'s health value is #{health} as of #{currentTime}"
end

def currentTime()
    Time.now.strftime("%I:%M:%S")
end
name1 = 'larry'
health1 = 60
name2 = 'curly'
health2 = 125
name3 = 'moe'
health3 = 100
name4 = 'shemp'
health4 = '90'
puts printHealth(name1, health1)
puts printHealth(name2, health2)
puts printHealth(name3, health3)
puts printHealth(name4, health4)

puts "#{name1.capitalize}'s health value is #{health1}."
puts "#{name2.upcase}'s health value is #{health2}."
puts "#{name3.capitalize}'s health is #{health3}.".center(30,'*')
puts "#{name4.capitalize.ljust(20,'.')} #{health4} health."

puts "Players:\n\t#{name1.capitalize}\n\t#{name2}\n\t#{name3}"

puts 123.to_s.reverse

