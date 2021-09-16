import SLMain
import SLStats
import SLForest
import time

inv = ["compass","Watch"]

def filled () :
    print("You have" + SLStats.invw + "amount of space left with you.")


def empty () :
    print("You don't any storage space left")

def remove() :

 print("You have surpassed your weight limitations")
 time.sleep(1)
 print("Please remove items from your inventory to remove space")
 time.sleep(2)
 print(inv)
 time.sleep(3)
 print("What would you like to remove from your inventory?")
 time.sleep(0.5)
 print(inv)
 length = len(inv)
 print ("You have" + length + "amount of items in your inventory..")
 ri = int(input(print("Which item would you like to remove from 1 to" + length)))

 while ri <= length and ri >= 0 :
       rt = ri - 1
       print("The item" + inv[rt] + "has been removed.")
       del inv[rt]
       time.sleep(1)
       print("You currently have these items")
       time.sleep(1.5)
       print(inv)     
       break
       
 while ri > length and ri < 0 :
     print("Please select a valid entry in your list.")
     time.sleep(1)
     ri= int(input("What would you like to remove from your inventory?")) 
     length = len(inv)
      
     if ri <= length and ri >= 0 :
         rt = ri - 1
         print("The item" + inv[rt] + "has been removed.")
         del inv[rt]
         time.sleep(1)
         print("You currently have these items")
         time.sleep(1.5)
         print(inv)     
         break
     


    