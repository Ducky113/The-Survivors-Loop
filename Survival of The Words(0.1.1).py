# Making a game for the first time
import time
import random
import sys

days = [10,11,12,13,14,15]
survivetill = 86400 * random.choice(days)

Survived = 64800
#INTRODUCTION


print ("Welcome to Survival of the Words......")
time.sleep(2.5)
name= input("what might your name be traveller?... " )
time.sleep(1)
print(name,",that's a good name you got there.")
time.sleep(1.5)
print("To start your adventure I would like to know what you would like your attributes to be..")
time.sleep(3)
print("To put it simply, you have 10 stat points, these can be used to level up your character's abilities")
time.sleep(3)
print(" you have six attributes namely,")
time.sleep(0.5)
print("Intellegence")
time.sleep(0.5)
print("Mental Endurance")
time.sleep(0.5)
print("Weight")
time.sleep(0.5)
print("Physique")
time.sleep(0.5)
print("Speed")
time.sleep(0.5)
print("Luck")
time.sleep(3)
print("You have to now give me the values you would like to assign to each of these attributes")
time.sleep(3)
print("I also want it to not exceed the 10 stat points I have supplied to you ")
time.sleep(1)



#PLAYER STATS (TO TOTAL UPTO 10)

intel= int(input("what would you like your stats for intellegence to be?"))
time.sleep(1)
print("So", intel, "for intellegence.")
time.sleep(0.5)
luck= int(input("What would you like your stats for luck to be?"))
time.sleep(1)
print("So",luck,"for luck.")
time.sleep(0.5)
stam= int(input("What would you like your stats for stamina to be?"))
time.sleep(1)
print("So",stam,"for stamina.")
time.sleep(0.5)
strength= int(input("What would you like your stats for Physique to be?"))
time.sleep(1)
print("So",strength,"for physique.")
time.sleep(0.5)
speed = int(input("What would you like your stats for speed to be?"))
time.sleep(1)
print("So",speed,"for speed.")
time.sleep(0.5)
mental= int(input("What would you like your stats for Mental Endurance to be?"))
time.sleep(1)
print("So", mental, "for mental endurance.")



#CHECK FOR CORRECT USAGE OF STAT POINTS
Stat= mental+speed+strength+intel+luck+stam


#Tally of Stat points used in total
while Stat!= 10: 
    print("your total doesn't use all the points or uses more than what was given.")
    time.sleep(1)
    print("please try again")
    time.sleep(2)
    intel= int(input("what would you like your stats for intellegence to be?"))
    time.sleep(1)
    print("So", intel, "for intellegence.(points remaining", 10-intel , ")")
    time.sleep(0.5)
    luck= int(input("What would you like your stats for luck to be?"))
    time.sleep(1)
    print("So",luck,"for luck.(points remaining", 10-intel-luck , ")")
    time.sleep(0.5)
    stam= int(input("What would you like your stats for stamina to be?"))
    time.sleep(1)
    print("So",stam,"for stamina.(points remaining", 10-intel-luck-stam , ")")
    time.sleep(0.5)
    strength= int(input("What would you like your stats for Strength to be?"))
    time.sleep(1)
    print("So",strength,"for physique.(points remaining", 10-intel-luck-stam , ")")
    time.sleep(0.5)
    speed = int(input("What would you like your stats for speed to be?(points remaining", 10-intel-luck-strength-speed , ")"))
    time.sleep(1)
    print("So",speed,"for speed.(points remaining", 10-intel-luck-strength-stam , ")")
    time.sleep(0.5)
    mental= int(input("What would you like your stats for Mental Endurance to be?"))
    time.sleep(1)
    print("So", mental, "for mental endurance.(points remaining", 10-intel-luck-strength-speed-mental-stam , ")")


    if Stat==10:
        break



#    Strength stats for amount of weight you can carry 
invw = float()
if strength == 0 :
     invw = 20.0  
elif strength == [1,2] :
     invw = 22.0
elif strength == [3,4] :
     invw = 25.0
elif strength == [5,6] :
     invw = 30.0
elif strength == [7] :
     invw = 35.0
elif strength == 8 :
     invw = 37.5
elif strength == 9 :
     invw = 40.0
elif strength == 10 :
     invw = 45.0 



#THE GAME STARTS

print("Well that takes care of the introduction. Let's start your journey.")
time.sleep(2)
print("all the best.")
time.sleep(1)
print("you wake up in a car, looks vaugely similar to you almost like you owned it at some point...")
time.sleep(3)
print("you look around and find a compass and a watch on your wrist.")
time.sleep(1)
print("the time says 6:00 p.m.")
survivetill = survivetill - 64800
time.sleep(0.5)
print("+ compass")
time.sleep(0.4)
print("+ watch")
time.sleep(1)
print("(Tip: You can use 'inv' when facing a choice to check your inventory.)")
time.sleep(1)
print(".....you get out of the car and notice that the engine of your car is broken and beyond repair")
time.sleep(2)



#Your Interpretation changes on the basis of your intellegence as follows :


if intel== [0,1] :
    print("'Yeah this shit's waaayyyy outta my league.', you say to yourself.")
    
elif intel == [2,3] :
  print("In your current situation you know that it's beyond repair")
elif intel ==[4,5] :
    print("You can see some holes in the pipes going into the engine, maybe that's what causing the problem")
    time.sleep(2)
    print("'A roll of electrical tape could probably do the work', you say to yourself")
    time.sleep(1)
    print("If you can find one that is.....................")

elif intel == [6,7,8,9,10] :
    print ("'From the looks of it the inlet valve for the petrol has been cut at several places', you say to yourself")
    time.sleep(3)
    print("but the marks look like they have been done by hand with something sharp")
    time.sleep(1)
    print("This leads you to believe that this inlet valve was cut by someone with an intention to damage the vehicle.")



#First Choice


time.sleep(2)
print("What would you like to do?")
time.sleep(1)
print("1. Search the car for supplies and resources. (30 minutes)")
time.sleep(0.5)
print("2. Go into the forest.(30 minutes)")
time.sleep(0.5)
ch1 = input(print("1 . 2 . inv"))
inv = ["compass","watch"]



if ch1 == 1:
    print("You decide to search the car for supplies and resources.")
    time.sleep(2)
    print("You find a piece of metal that can be used as a makeshift knife")
    time.sleep(2)
    print("+ makeshift knife")
    inv.extend(['Makeshift Knife'])
    time.sleep(0.5)
    print( "You also take the cover of the seat belts to be of use in the future.")
    time.sleep(0.5)
    print( "+ cloth")
    survivetill = survivetill - 1800
    inv.extend(['5 pieces of cloth'])


if ch1== 2:
    print("You venture into the forest")
    time.sleep(1)
    print("You can see some small trees that can be harvested for some wood.")
    time.sleep(2)
    print("You can also notice some rocks and sticks that might come in handy.")
    time.sleep(1)
    print("What would you like to do?")
    survivetill = survivetill - 1800
    time.sleep(1)
    print("1. Collect some sticks. (5 minutes)")
    print("2. Collect some rocks. (5 minutes)")
    print("3. Collect both rocks and sticks. (7 and a half minutes)")
    print("4. Venture further into the forest. (1 hour)")        
    ch2 = input(print("1 . 2. 3 . 4 . inv"))


    while ch2 == 1 :
        print("You collect some sticks...... (6:35 p.m.)")
        time.sleep(0.5)
        print ("+ 5 sticks ")
        time.sleep(0.5)
        print("- 0.1 kg of storage space.")
        time.sleep(0.5)
        print("1. Collect some sticks. (5 minutes)")
        time.sleep(0.5)
        print("2. Collect some rocks. (5 minutes)")
        time.sleep(0.5)
        print("3. Collect both rocks and sticks. (7 and a half minutes)")
        time.sleep(0.5)
        survivetill = survivetill - 300
        print("4. Venture further into the forest. (1 hour)") 
        inv.extend(['5 sticks'])
        invw = invw - 0.1


        if invw> 0 :
            print("You have" + invw + "amount of space left with you.")
        elif invw == 0 :
         print("You don't any storage space left")
        while invw<0 :
          print("You have surpassed your weight limitations")
          time.sleep(1)
          print("Please remove items from your inventory to remove space")
          time.sleep(2)
          print(inv)
          time.sleep(3)
          print("What would you like to remove from your inventory?")
          time.sleep(0.5)
          print(inv)
          x = len(inv)
          print ("You have" + x + "amount of items in your inventory..")
          y = int(input(print("Which item would you like to remove from 1 to" + x)))
          y= x-1



          while y<0 or y>=x :
             print("Please select a valid entry in your list.")
             rt = int(input("What would you like to remove from your inventory?")) 
             rt= x-1



             if rt>=0 or rt<x :
                   print("The item on inventory number" + x + "has been removed.")
                   del inv[x]
                   print("You currently have these items")
                   print(inv)



        ch2 = input(print("1 . 2. 3 . 4 . inv"))
        if ch2 == [2,3,4, "inv"] :
            break



    while ch2==2 :
        print ("You collect some rocks.......(6:35 p.m.")
        time.sleep(0.5)
        print ("+ 5 rocks ")
        time.sleep(0.5)
        print("- 0.2 kg of storage space.")
        time.sleep(0.5)
        print("1. Collect some sticks. (5 minutes)")
        time.sleep(0.5)
        print("2. Collect some rocks. (5 minutes)")
        time.sleep(0.5)
        print("3. Collect both rocks and sticks. (7 minutes)")
        time.sleep(0.5)
        print("4. Venture further into the forest. (1 hour)") 
        time.sleep(0.5)
        inv.extend(['5 rocks'])
        invw = invw - 0.2
        if invw> 0 :
            print("You have" + invw + "amount of space left with you.")
        elif invw == 0 :
         print("You don't any storage space left")
        while invw<0 :
          print("You have surpassed your weight limitations")
          time.sleep(1)
          print("Please remove items from your inventory to remove space")
          time.sleep(2)
          print(inv)
          time.sleep(3)
          print("What would you like to remove from your inventory?")
          time.sleep(0.5)
          print(inv)
          x = len(inv)
          print ("You have" + x + "amount of items in your inventory..")
          y = int(input(print("Which item would you like to remove from 1 to" + x)))
          y= x-1



          while y<0 or y>=x :
             print("Please select a valid entry in your list.")
             rt = int(input("What would you like to remove from your inventory?")) 
             rt= x-1



             if rt>=0 or rt<x :
                   print("The item on inventory number" + x + "has been removed.")
                   del inv[x]
                   print("You currently have these items")
                   print(inv)



        ch2 = input(print("1 . 2. 3 . 4 . inv"))
        if ch2==[1,3,4, "inv"] :
            break
            
    while ch2==3 :
        print("You collected both rocks and sticks......(6:37 p.m.)")
        time.sleep(0.5)
        print(" + 5 rocks")
        time.sleep(0.5)
        print("+ 5 sticks")
        time.sleep(0.5)
        print("- 0.3 kg of storage space")
        time.sleep(0.5)
        print("1. Collect some sticks. (5 minutes)")
        time.sleep(0.5)
        print("2. Collect some rocks. (5 minutes)")
        time.sleep(0.5)
        print("3. Collect both rocks and sticks. (7 minutes)")
        time.sleep(0.5)
        print("4. Venture further into the forest. (1 hour)") 
        time.sleep(0.5)
        inv.extend(['5 sticks'])
        inv.extend(['5 rocks'])

        if invw> 0 :
            print("You have" + invw + "amount of space left with you.")
        elif invw == 0 :
         print("You don't any storage space left")
        while invw<0 :
          print("You have surpassed your weight limitations")
          time.sleep(1)
          print("Please remove items from your inventory to remove space")
          time.sleep(2)
          print(inv)
          time.sleep(3)
          print("What would you like to remove from your inventory?")
          time.sleep(0.5)
          print(inv)
          x = len(inv)
          print ("You have" + x + "amount of items in your inventory..")
          y = int(input(print("Which item would you like to remove from 1 to" + x)))
          y= x-1



          while y<0 or y>=x :
             print("Please select a valid entry in your list.")
             rt = int(input("What would you like to remove from your inventory?")) 
             rt= x-1



             if rt>=0 or rt<x :
                   print("The item on inventory number" + x + "has been removed.")
                   del inv[x]
                   print("You currently have these items")
                   print(inv)



        ch2 = input(print("1 . 2. 3 . 4 . inv"))
        if ch2 != 3 :
            break

    while ch2== "inv" :
        print("Your inventory currently contains......")
        time.sleep(0.5)
        print(inv)
        if ch2 ==[1,2,3,4]:
            break

    
             