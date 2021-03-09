import random 
rockbot = random.randint(1,3)
# print(rockbot)

print("Lisa Simpson - 'Poor predictable Bart, always chooses rock.'")
print("Bart Simpson - 'Come on rock. Nothing beats rock.'\n")

print(" __||||||__")
print("|          |")
print("[ {-}  {-} ]")
print("[    __    ]")
print("|          |")
print("|  \____/  |")
print(" \________/") 

print("\nSuuupp! I'm Rockbot!!\n\n\nLet's play Rock Paper Scissors!!!")
print("\nJust type in your choice.")
print("\nOk. I'm ready. Good to go? On three...\n\nOne.\n\nTwo!\n")
player = input("Three!!\n\n")
player = player.lower()

print("\nYou chose",player,".")
if(rockbot == 1):
  print("I chose rock.")
elif(rockbot == 2):
  print("I chose paper.")
elif(rockbot == 3):
  print("I chose scissors.")

if(player == "rock"):
  player = 1
elif(player == "paper"):
  player = 2 
elif(player == "scissors"):
  player = 3

if(rockbot == player):              ## change this to a while loop, maybe
  print("\nIt's a draw!")
elif(rockbot + player == 4):
  print("\nRock beats scissors.")
  if(rockbot == 1):
    print("I win!")
  elif(player == 1):
    print("You win!")  
elif(rockbot + player == 5):
  print("\nScissors beat paper.")
  if(rockbot == 3):
    print("I win!")
  elif(player == 3):
    print("You win!") 
elif(rockbot + player == 3):
  print("\nPaper beats rock.")
  if(rockbot == 2):
    print("I win!")
  elif(player == 2):
    print("You win!") 

print("\n\nShall we play again?")
## how to keep score, creat a list? score = score + 1
