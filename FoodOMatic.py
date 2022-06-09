'''
Created on Nov 3, 2021

@author: Noah Sokol
Description: Generates ammount of foods you ask for then tells you how much they cost
Bonuses: pick how many foods you want, asks if want to play again, attempted to tell cost
Bugs: cost is sometimes innacurate

'''
import random                                               #imports random
import time                                                 #imports time
y = 0
prepaired = ('local ', 'roasted ', 'grilled ', 'garlic mashed ', 'oven dried ', 'spiced ', 'stewed ','assorted ','iced ','sliced ','braised ','free-range ','baby ','teriyaki glaced ','steamed ',)
food = ('cauliflower ','tilapia fillet ','pork loin ','green beans ', 'basmati rice ','rainbow carrots ','fingerling potatoes ','three color squash ','potatoes ','eggplant ','drumstick ','short rib ','duck brest ','eye round beef ','baguette ')
extra = ('with fennel','gratin','bengali style', 'with peas','pizza','with balsamico','with garlic and olive oil', 'with pigeon peas', 'with minted yogurt','soup','chutney','salad','with tropical fruit salsa','over sticky rice','au jus')
while y == 0:
    x = 0                                                   #so the while loop stays true until changed                                              #loop for if the user inputs anything other than numbers
    amount = input("How many foods would you like? ")       #asking many foods user wants
    try:                                                    #trying to convert how many foods the person wants to an int
        amount = int(amount)                                #converting amount to an int so i can be added to
        foodcost = 0 
        for x in range (0,amount):                          #looping it to generate a food a specific ammount of times
            adjective = random.choice (prepaired)           #random prepaired
            noun = random.choice (food)                     #random food
            addon = random.choice (extra)                   #random extra
            print (adjective + noun + addon)                #printing the food
            time.sleep (0.2)                                #makes information print slower
            if adjective == ('oven dried ') or adjective == ('assorted '):  #saying if it is roasted or assorted its an extra 5$ for each of these lines 
                foodcost = foodcost + 5
            elif adjective == ('garlic mashed ') or adjective == ('braised '):
                foodcost = foodcost + 4
            elif adjective == ('grilled ') or adjective == ('spiced ') or adjective == ('teriyaki glaced ') or adjective == ('steamed '):
                foodcost = foodcost + 3
            elif adjective == ('roasted ') or adjective == ('stewed ') or adjective == ('assorted ') or adjective == ('iced ') or adjective == ('sliced ') or adjective == ('braised ') :
                foodcost = foodcost + 2     
            elif adjective == ('local ') or adjective == ('free-range ') or adjective == ('baby '):
                foodcost = foodcost + 1
            else:
                foodcost = foodcost + 0
            if noun == ('tilapia fillet ') or noun == ('pork loin ') or noun == ('drumstick ') or noun == ('short rib ') or noun == ('duck breast ') or noun == ('eye of round beef '):
                foodcost = foodcost + 20
            elif noun == ('three color squash ') or noun == ('rainbow carrots ') or noun == ('fingerling potatoes ') or noun == ('baguette '):
                foodcost = foodcost + 10
            elif noun == ('cauliflower ') or noun == ('green beans ') or noun == ('basmati rice ') or noun == ('potatoes ') or noun == ('eggplant '):
                foodcost = foodcost + 5
            else:
                foodcost = foodcost + 0
        while y == 0:                                       #to make sure they input either yes or no
            foodcost = str(foodcost)                        #converting foodcost to a string so it can be printed
            print ("your food is " + foodcost + "$ ")       #printing the cost of the food
            again = input('again? ').lower()                #asking if they want to play again and putting in lowercase
            if again == ('no'):                             #if they dont want to play again print bye and break the loop
                print ('goodbye')
                y = 1                                       #to break the while loop of asking again
                break                                       #breaks entire loop of asking how many foods they want
            if again == ('yes'):                            #if they do want to play again break loop of asking again
                break                                       #breaks loops of asking again
            else:                                           #if they don't put in yes or no then ask them to print again
                print ('please input yes or no ')
    except ValueError:                                      #if the user inputs a letter
        print ('Please enter a number')