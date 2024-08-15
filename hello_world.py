print("Hello!")
print("What food do you like?")
x = input()
if x.lower() == "pasta":
    print("HI PASTA LOVER!")
else:
    print("NOOOOO WRONG ANSWER!!! DID YOU MEAN PASTA?")

percent = int(input("Enter quiz score  "))

if percent == 100:
  print("Here Is 30$ !")
  print("Telling Mom And Dad..............")
elif percent >= 90:
  print("Here Is your 20$.")
  print("Telling Mom And Dad..............")
elif percent >= 75:
  print("Here Is your 10$.")
  print("Telling Mom And Dad..............")
else:
  print("Great effort!")
  print ("Telling Mom And Dad..............")
  print ("Add teacher note")

print ("Did the teacher keep you in for recces?")
k = input()

if k.lower() == "no":
    print("Yeah, good job. Telling Mom and Dad.")

elif k.lower() == "yes, sorry. ":
   
  print("Its alright.")
   
else :
    print("Not good, Telling Mom and Dad........")
    print("Add teacher note.")
    
print("Ok here is your homework.")  

fin_lit = "Financial Literacy"
pixar = "Pixar in a Box"
grammar = "Grammar"

# Collect user attributes to inform our recommendation.
grade = int(input("What grade are you in? "))
favorite_subject = input("What is your favorite subject? ")

# Make a course recommendation based on the user's attributes.
rec = ""
if grade < 6:
    # Course caters to younger learners.
    rec = grammar
else:
    if favorite_subject == "computing" or favorite_subject == "art":
        rec = pixar
    else:
        # Most broadly relevant and approachable subject.
        rec = fin_lit

print("We recommend this course: " + rec)
