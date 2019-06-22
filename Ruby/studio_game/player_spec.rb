require_relative 'spec_helper'
require_relative 'player'

describe Player do

    before do
        @player = Player.new("larry", 150)
        @weakPlayer = Player.new("moe", 100)
        @initialHealth = @player.health
        $stdout = StringIO.new
    end

    it "has a capitalized name" do
        expect(@player.name).to eq("Larry")
    end

    it "has an initial health" do
        expect(@player.health).not_to eq(nil)
    end

    it "has a string representation" do
        expect(@player.to_s).to be_a(String)
    end

    it "score is sum of health and length of name" do
        expectedScore = @player.health + @player.name.length
        expect(@player.score).to eq(expectedScore)
    end

    it "increases health by 15 when w00ted" do
        @player.w00t 
        expect(@player.health).to eq(@initialHealth + 15)
    end

    it "decreases health by 10 when blammed" do
        startHealth = @player.health
        @player.blam 
        expect(@player.health).to eq(@initialHealth - 10)
    end

    it "player is strong" do
        expect(@player.strong?).to eq(true)
    end
    it "weak player is not strong" do
        expect(@weakPlayer.strong?).to eq(true)
    end
end
