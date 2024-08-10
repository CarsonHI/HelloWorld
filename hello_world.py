print("Hello!")
print("What food do you like?")
x = input()
if x.lower() == "pasta":
    print("HI PASTA LOVER!")
else:
    print("NOOOOO WRONG ANSWER!!! DID YOU MEAN PASTA?")

percent = int(input("Enter quiz score (out of 100): "))

if percent == 100:
  print("Here Is 30$ !")
  print("Telling Mom And Dad..............")
elif percent >= 90:
  print("Here Is your 20$")
  print("Telling Mom And Dad..............")
elif percent >= 75:
  print("Here Is your 10$")
  print("Telling Mom And Dad..............")
else:
  print("Great effort!")
  print ("Telling Mom And Dad..............")
percent = int(input("Enter quiz score (out of 100): "))