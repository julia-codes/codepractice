require_relative 'spec_helper'
require_relative 'practice'
#rspec practice_spec.rb

describe Practice do
    before do
        #setup before testing
        @value =  "something"
        @default_practice = Practice.new()
        @practice = Practice.new("Special Name",3)
    end



    it "has a thing I want to test" do
        expect(@value).to eq("something")
    end
    it "will have the practice initialized" do
        expect(@default_practice).not_to eq(nil)
    end
    it "will write the obj to a string" do
        expect(@practice.to_s).to be_a(String)
    end
    it "has a name that is directly readable" do
        expect(@practice.name).not_to eq(nil)
    end
    it "'s default name is Something" do
        expect(@default_practice.name).to eq("Something")
    end
    it "will return the modifier through a function" do
        expect(@practice.modifierStatus).to eq(3)
    end
    it "default modifier is 1" do
        expect(@default_practice.modifierStatus).to eq(1)
    end
    it "modifier is 1 then it returns One" do
        expect(@default_practice.modifierIsOne).to eq("One")
    end
    it "modifier is greater than 1 it returns More" do
        expect(@practice.modifierIsOne).to eq("More")
    end
    it "has an array" do
        expect(@practice.myArray).to be_a(Array)
    end
    
    it "allows to add to the array" do
        @practice.myArray.push(0)
        expect(@practice.myArray.length).to eq(1)
    end
    it "allows to remove from the array" do
        @practice.myArray.push(0)
        puts "with one thing: #{@practice.myArray}"
        puts "return from pop:  #{@practice.myArray.pop()}"
        puts "empty array: #{@practice.myArray}"
        expect(@practice.myArray.length).to eq(0)
    end
    it "allows to get the length of the array"
    it "will add the length of array to modifier"
    it "will multiply the length of array times modifier"
    it "will allow to loop through the array and print contents"
end