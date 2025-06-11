import random

while(True):
   computer = random.choice([-1,0,1])
   youstr = input("Enter your choice r/p/s:").lower()

   Dict = { "r":-1,"p":0,"s":1}
   revDict = {-1:"Rock",0:"Paper",1:"Scissor"}
   
   if youstr not in Dict:
     print("Invalid Input! Please select from r/p/s.")
     continue
   
   you = Dict[youstr]

   print(f"You choose {revDict[you]} and Computer choose {revDict[computer]}")

   if(you == computer):
      print("It's a draw!")
   
   elif((you==-1 and computer==1) or
        (you==0 and computer==-1 ) or
        (you==1 and computer==0)):
      print("You Win!")
    
   else:
      print("You Lose!")

   again = input("Want to Play Again? (y/n):").lower()
   if again != "y":
     break
     
   