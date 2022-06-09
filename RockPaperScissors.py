'''
Created on Oct 26, 2021
Description: Plays rock paper scissors
log 1.0
@author: NSokol25
Bonus: Asks how many games you want to play, can play again, scoreboard
'''

import random
again = ('yes')
playerscore = 0 
computerscore = 0
while again == ('yes'):                                             #looping all of code in case someone inputs neither a number or letters not unlimited
    games = input("how many games would you like to play? If unlimited enter unlimited: ")#asking how many games or unlimited games user wants to play
    try:                                                            #checking if user input a number by seeing if it can be converted to an int
        games = int(games)
        for x in range (0,games):                                   #loop
            while again ==('yes'):
                player = input("pick rock, paper, or scissors ").lower()   #asking player for rock paper scissors
                computer = ('rock', 'paper', 'scissors')            #generates rock paper or scissors
                computer = random.choice (computer)
                playerscore = int(playerscore)                      #converting them back into intengers so they can 
                computerscore = int(computerscore)                  #be added too for scoreboard
                print ("player picks " + player + " computer picks " + computer)
                if computer == player:                              #if there's a tie
                    print ("tie")
                elif computer == ('paper') and player == ('rock'):  #if computer is rock and player is paper
                    print ("computer wins")
                    computerscore = computerscore + 1               #adding one to the computer's score
                elif computer == ('paper') and player == ('scissors'):#all scenarios
                    print ("player wins")
                    playerscore = playerscore + 1                   #adding one to the player's score
                elif computer == ('scissors') and player == ('paper'):
                    print ("computer wins")
                    computerscore = computerscore + 1
                elif computer == ('scissors') and player == ('rock'): 
                    print ("player wins")
                    playerscore = playerscore + 1
                elif computer == ('rock') and player == ('scissors'):
                    print ("computer wins")
                    computerscore = computerscore + 1
                elif computer == ('rock') and player == ('paper'):
                    print ("player wins")
                    playerscore = playerscore + 1
                else: 
                    print ("try again")
                    continue
                playerscore = str(playerscore)                      #converting variable playerscore and computerscore 
                computerscore = str(computerscore)                  #so they can be printed
                print ("player " + playerscore + " computer " + computerscore)   #scoreboard
                break
        playerscore = int(playerscore)
        computerscore = int(computerscore)
        if (computerscore) < (playerscore):                     #seeing who won
            playerscore = str(playerscore)                      #converting variable playerscore and computerscore 
            computerscore = str(computerscore)                  #so they can be printed
            print ('\nplayer wins!\nPlayer ' + playerscore + ' Computer ' + computerscore)
        if (playerscore) < (computerscore):                       #seeing who won
            playerscore = str(playerscore)                      #converting variable playerscore and computerscore 
            computerscore = str(computerscore)                  #so they can be printed
            print ('\ncomputer wins!\nComputer ' + computerscore + ' Player ' + playerscore) 
        if (playerscore) == (computerscore):                    #if tie
            playerscore = str(playerscore)                      #converting variable playerscore and computerscore 
            computerscore = str(computerscore)                  #so they can be printed
            print ('\ntie!\nPlayer ' + playerscore + ' Computer ' + computerscore)
        print ('bye')
        break
                
    
        
    except ValueError:                                              #what happens if the input not a number
        if games == ('unlimited'):
            again = ('yes')
            playerscore = 0 
            computerscore = 0
            while again == ('yes'):                                 #loop
                player = input("pick rock, paper, or scissors ").lower()   #asking player for rock paper scissors
                computer = ('rock', 'paper', 'scissors')            #generates rock paper or scissors
                computer = random.choice (computer)
                playerscore = int(playerscore)                      #converting them back into intengers so they can 
                computerscore = int(computerscore)                  #be added too for scoreboard
                print ("player picks " + player + " computer picks " + computer)
                if computer == player:                              #if there's a tie
                    print ("tie")
                elif computer == ('paper') and player == ('rock'):  #if computer is rock and player is paper
                    print ("computer wins")
                    computerscore = computerscore + 1               #adding one to the computer's score
                elif computer == ('paper') and player == ('scissors'):#all scenarios
                    print ("player wins")
                    playerscore = playerscore + 1                   #adding one to the player's score
                elif computer == ('scissors') and player == ('paper'):
                    print ("computer wins")
                    computerscore = computerscore + 1
                elif computer == ('scissors') and player == ('rock'): 
                    print ("player wins")
                    playerscore = playerscore + 1
                elif computer == ('rock') and player == ('scissors'):
                    print ("computer wins")
                    computerscore = computerscore + 1
                elif computer == ('rock') and player == ('paper'):
                    print ("player wins")
                    playerscore = playerscore + 1
                else: 
                    print ("try again")
                    continue
                playerscore = str(playerscore)                      #converting variable playerscore and computerscore 
                computerscore = str(computerscore)                  #so they can be printed
                print ("player " + playerscore + " computer " + computerscore)   #scoreboard
                another = input("play again? ")                     #see if users wants to play again
                if another == ('no'):                               #if not break the loop and end the game
                    playerscore = int(playerscore)
                    computerscore = int(computerscore)
                    if (computerscore) < (playerscore):                     #seeing who won
                        playerscore = str(playerscore)                      #converting variable playerscore and computerscore 
                        computerscore = str(computerscore)                  #so they can be printed
                        print ('\nplayer wins!\nPlayer ' + playerscore + ' Computer ' + computerscore)
                    if (playerscore) < (computerscore):                       #seeing who won
                        playerscore = str(playerscore)                      #converting variable playerscore and computerscore 
                        computerscore = str(computerscore)                  #so they can be printed
                        print ('\ncomputer wins!\nComputer ' + computerscore + ' Player ' + playerscore) 
                    if (playerscore) == (computerscore):                    #if tie
                        playerscore = str(playerscore)                      #converting variable playerscore and computerscore 
                        computerscore = str(computerscore)                  #so they can be printed
                        print ('\ntie!\nPlayer ' + playerscore + ' Computer ' + computerscore)
                    print ("bye")
                    break
                else: again = ('yes')
            break
                
        else:
            print("Please enter either a number or unlimited ")