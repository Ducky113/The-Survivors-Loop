# Making a game for the first time
import time
import random
import sys
import SLForest
import SLInv
import SLStats

days = (10,11,12,13,14,15)
survivetill = 1440 * random.choice(days)
Survived = 1080

def gametime(g) :
    global survivetill
    global Survived
    g = int()
    survivetill= survivetill  - g
    Survived = Survived + g
    minutes = Survived % 60
    hoursmin = Survived - minutes
    thours = hoursmin/60
    hours = thours % 24
    dayhours = thours - hours
    day = dayhours/24
    
    print("The time currently is " + str(int(hours)), str(int(minutes))+ " hours")
    time.sleep (1)
    print ("it's day " + str(int(day)))
    

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
    tp = intel
    print("So", intel, "for intellegence.(points remaining "+ str(10-tp) + ")")
    time.sleep(0.5)
    luck= int(input("What would you like your stats for luck to be?"))
    time.sleep(1)
    tp = tp + luck
    print("So",luck,"for luck.(points remaining " + str(10 - tp) + ")")
    time.sleep(0.5)
    stam= int(input("What would you like your stats for stamina to be?"))
    time.sleep(1)
    tp = tp + stam
    print("So",stam,"for stamina.(points remaining "+ str(10 - tp) + ")")
    time.sleep(0.5)
    strength= int(input("What would you like your stats for Strength to be?"))
    time.sleep(1)
    tp = tp + strength
    print("So",strength,"for physique.(points remaining " + str(10-tp) + ")")
    time.sleep(0.5)
    speed = int(input("What would you like your stats for speed to be?(points remaining "+ str(10-tp) + ")"))
    time.sleep(1)
    tp = tp + speed
    print("So",speed,"for speed.(points remaining "+ str(10- tp) + ")")
    time.sleep(0.5)
    mental= int(input("What would you like your stats for Mental Endurance to be?"))
    time.sleep(1)
    tp = tp + mental
    print("So", mental, "for mental endurance.(points remaining "+ str(10-tp) + ")")


    if tp == 10 :
        break

exec("SLStats.invweight")
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
survivetill = survivetill - 1080
time.sleep(0.5)
print("+ compass")
time.sleep(0.4)
print("+ watch")
time.sleep(1)
print("(Tip: You can use 'inv' when facing a choice to check your inventory.)")
time.sleep(1)
print(".....you get out of the car and notice that the engine of your car is broken.")

while intel == intel :

 if intel== (0,1) :
     print("'Yeah this shit's waaayyyy outta my league.', you say to yourself.")
    
 elif intel == (2,3) :
   print("In your current situation you know that it's beyond repair")

 elif intel ==(4,5) :
     print("You can see some holes in the pipes going into the engine, maybe that's what causing the problem")
     time.sleep(2)
     print("'A roll of electrical tape could probably do the work', you say to yourself")
     time.sleep(1)
     print("If you can find one that is.....................")

 elif intel == (6,7,8) :
     print ("'From the looks of it the inlet valve for the petrol has been cut at several places', you say to yourself")
     time.sleep(3)
     print("but the marks look like they have been done by hand with something sharp")

 elif intel == (9,10) :
     print ("'From the looks of it the inlet valve for the petrol has been cut at several places', you say to yourself")
     time.sleep(3)
     print("but the marks look like they have been done by hand with something sharp")
     time.sleep (0.5)
     print("This leads you to believe that this inlet valve was cut by someone with an intention to damage the vehicle.")  
 break


#First Choice


time.sleep(2)
print("What would you like to do?")
time.sleep(1)
print("1. Search the car for supplies and resources. (30 minutes)")
time.sleep(0.5)
print("2. Go into the forest.(30 minutes)")
time.sleep(0.5)
ch1 = input(print("1 . 2 . inv"))



if ch1 == "1":
    print("You decide to search the car for supplies and resources.")
    time.sleep(2)
    print("You find a piece of metal that can be used as a makeshift knife")
    time.sleep(2)
    print("+ makeshift knife")
    SLInv.inv.extend(['Makeshift Knife'])
    time.sleep(0.5)
    print( "You also take the cover of the seat belts to be of use in the future.")
    time.sleep(0.5)
    print( "+ 5 pieces of cloth")
    SLInv.inv.extend(['5 pieces of cloth'])
    gametime(30)
    print("What would you like to do next?")
    time.sleep(0.5)
    print("1. Take some rest in your car. (4 hours)")
    print("2. Go into the woods (30 minutes) ")
    ch0 = str(input("1 . 2 . inv"))

    while ch0 == "1" :
     print("You take a nap for 4 hours.")
     time.sleep(0.5)
     print("You have gained some of your strength back...")
     time.sleep(0.5)
     gametime(240)
     time.sleep(0.5)
     print("What would you like to do next?")
     time.sleep(0.5)
     print("1. Take some rest in your car. (4 hours)")
     print("2. Go into the woods (30 minutes) ")
     ch0 = str(input("1 . 2 . inv"))
     if ch0 == ["2","inv"] :
         break

    while ch0 == "inv" :
        print("Your inventory currently contains these items....")
        time.sleep(0.5)
        print (SLInv.inv)
        time.sleep(0.5)
        print("What would you like to do next?")
        time.sleep(0.5)
        print("1. Take some rest in your car. (4 hours)")
        print("2. Go into the woods (30 minutes) ")
        ch0 = str(input("1 . 2 . inv"))
        if ch0 == ["1","2"] :
            break
      
    if ch0 == "2" :
       ch1 == "2"


if ch1 == "2" :
     exec("SLForest.forestchoice0()")

     if SLStats.invw >= 0 :
         exec("SLInv.filled()")

     elif SLStats.invw == 0 :
         exec("SLInv.empty()")

     while SLStats.invw<0 :
         exec("SLInv.remove()")
        
     


     while ch2 == "1" :
         exec("SLForest.foreststicks()")

         if SLStats.invw >= 0 :
              exec("SLInv.filled()")

         elif SLStats.invw == 0 :
             exec("SLInv.empty()")

         while SLStats.invw<0 :
              exec("SLInv.remove()")


         print("1. Collect some sticks. (5 minutes)")
         time.sleep(0.5)
         print("2. Collect some rocks. (5 minutes)")
         time.sleep(0.5)
         print("3. Collect both rocks and sticks. (7 minutes)")
         time.sleep(0.5)
         print("4. Venture further into the forest. (1 hour)")
         ch2 = str(input("1 . 2. 3 . 4 . inv"))
         if ch2==["2","3","4", "inv"] :
             break
             

     while ch2=="2" :
         exec("SLForest.forestrocks()")
         if SLStats.invw >= 0 :
              exec("SLInv.filled()")

         elif SLStats.invw == 0 :
             exec("SLInv.empty()")

         while SLStats.invw<0 :
              ("SLInv.remove()")

        
         print("1. Collect some sticks. (5 minutes)")
         time.sleep(0.5)
         print("2. Collect some rocks. (5 minutes)")
         time.sleep(0.5)
         print("3. Collect both rocks and sticks. (7 minutes)")
         time.sleep(0.5)
         print("4. Venture further into the forest. (1 hour)")
         ch2 = input("1 . 2. 3 . 4 . inv")
         if ch2==["1","3","4", "inv"] :
             break
            
     while ch2=="3" :
         exec("SLForest.forestsr()")

         if SLStats.invw >= 0 :
              exec("SLInv.filled()")

         elif SLStats.invw == 0 :
             exec("SLInv.empty()")

         while SLStats.invw<0 :
              ("SLInv.remove()")

         print("1. Collect some sticks. (5 minutes)")
         time.sleep(0.5)
         print("2. Collect some rocks. (5 minutes)")
         time.sleep(0.5)
         print("3. Collect both rocks and sticks. (7 minutes)")
         time.sleep(0.5)
         print("4. Venture further into the forest. (1 hour)")
         ch2 = input("1 . 2. 3 . 4 . inv")
         if ch2==["1","2","4", "inv"] :
             break


     while ch2== "inv" :
         print ("SLInv.inv()")











    
             