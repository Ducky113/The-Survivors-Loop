# Making a game for the first time
import time
import random
import sys


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
strength= int(input("What would you like your stats for Strength to be?"))
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
while Stat!=10: 
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

print("Well that takes care of the introduction. Let's start your journey.")
time.sleep(2)
print("all the best.")
time.sleep(1)
print("you wake up in a car, looks vaugely similar to you almost like you owned it at some point...")
time.sleep(3)
print("you look around and find a compass and a watch on your wrist.")
time.sleep(1)
print("the time says 6:00 p.m.")
time.sleep(0.5)
print("+ compass")
time.sleep(0.4)
print("+ watch")
time.sleep(1)
print("(Tip: You can use 'inv' when facing a choice to check your inventory.)")
time.sleep(1)
print(".....")


