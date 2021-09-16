import time
import SLMain
import SLStats
import SLInv



def forestchoice0() :
 print("You venture into the forest")
 time.sleep(1)
 print("You can see some small trees that can be harvested for some wood.")
 time.sleep(2)
 print("You can also notice some rocks and sticks that might come in handy.")
 time.sleep(1)
 SLMain.gametime(30)
 time.sleep(0.5)
 print("What would you like to do?")
 time.sleep(1)
 print("1. Collect some sticks. (5 minutes)")
 print("2. Collect some rocks. (5 minutes)")
 print("3. Collect both rocks and sticks. (7 and a half minutes)")
 print("4. Venture further into the forest. (1 hour)")        


def foreststicks() :
 print("You collect some sticks......")
 time.sleep(0.5)
 print ("+ 5 sticks ")
 time.sleep(0.5)
 print("- 0.1 kg of storage space.")
 time.sleep(0.5)
 print("1. Collect some sticks. (5 minutes)")
 time.sleep(0.5)
 print("2. Collect some rocks. (5 minutes)")
 time.sleep(0.5)
 print("3. Collect both rocks and sticks. (7 minutes)")
 time.sleep(0.5)
 print("4. Venture further into the forest. (1 hour)") 
 time.sleep(0.5)
 SLMain.gametime(5)
 SLInv.inv.extend(['5 sticks'])
 SLStats.invw = SLStats.invw - 0.1


def forestrocks() :
    print ("You collect some rocks.......")
    time.sleep(0.5)
    print ("+ 5 rocks ")
    time.sleep(0.5)
    print("- 0.2 kg of storage space.")
    time.sleep(0.5)
    SLMain.gametime(5)
    time.sleep(0.5)
    print("1. Collect some sticks. (5 minutes)")
    time.sleep(0.5)
    print("2. Collect some rocks. (5 minutes)")
    time.sleep(0.5)
    print("3. Collect both rocks and sticks. (7 minutes)")
    time.sleep(0.5)
    print("4. Venture further into the forest. (1 hour)") 
    time.sleep(0.5)
    SLInv.inv.extend(['5 rocks'])
    SLStats.invw = SLStats.invw - 0.2


def forestsr() :
    print("You collected both rocks and sticks......")
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
    SLInv.inv.extend(['5 sticks'])
    SLInv.inv.extend(['5 rocks'])
    SLMain.gametime(7)