import SLMain
#    Strength stats for amount of weight you can carry 

def invweight() :
 invw = float()
 if SLMain.strength == 0 :
      invw = 20
 elif SLMain.strength == (1,2) :
      invw = 22
 elif SLMain.strength == (3,4) :
      invw = 25
 elif SLMain.strength == (5,6) :
      invw = 30
 elif SLMain.strength == (7) :
      invw = 35
 elif SLMain.strength == 8 :
      invw = 37.5
 elif SLMain.strength == 9 :
      invw = 40
 elif SLMain.strength == 10 :
      invw = 45 

