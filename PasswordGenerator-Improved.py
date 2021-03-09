
import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?&@£$%"
mylist = ["yes", "yes please", "yes, please", "yeah", "sure", "ok", "yep", "affermative", "do it", "go ahead", "go for it", "knock yourself out"]

print(" __________")
print("|          |")
print("| (O)  (O) |")
print("|    []    |")
print("|  ______  |")
print("|  \____/  |")
print("|__________|\n")
print("Hello!\n\nI'm Passbot. \n\nI can create ten new passwords for you.\n")

begin = input("Shall I create some now?\n")
begin = begin.lower()
if (begin in mylist):
  print("\nOk, here they are:\n")
else:
  print("Oh, well, I have no purpose now.....\n\n\n\n\n....here's some passwords for you anyway:\n")

for p in range (0, 10):
  password = ""
  for c in range(12):
    password += random.choice(chars)
  print(password)

more = input("\nIf those aren't any good, I can make ten more. Would you like that? ")
more = more.lower()
if (more in mylist):
  print("\nHere's ten more passwords for you:\n")
  for p in range (0, 10):
    password = ""
    for c in range(12):
      password += random.choice(chars)
    print(password)

  repeat = input("\nWould you still like more? ")
  repeat = repeat.lower()
  while (repeat in mylist):
    print("\nAnd here's some more:\n")
    for p in range (0, 10):
      password = ""
      for c in range(12):
        password += random.choice(chars)
      print(password)
    repeat = input("\nSome more? ")
    repeat = repeat.lower()
else:
  print("\nAlrighty then.")
print("\nI guess my work here is done.\n\nBut before I go, please be so kind as to tell me how happy you are with your experience today.")

feedback = input("You can give me a score out of 10.\nWith 10 being 'absolutely delighted' and 0 being 'miserably depressed'.\n")
feedback = int(feedback)
if (feedback >= 7):
  print("\nHappy to be of service!")
elif (feedback <= 4): 
  print("\nAh... really?! Shit... sorry...")
else:
  print("\nHmm, Ok. Room for improvement then...\n")
print("See you next time.\n")