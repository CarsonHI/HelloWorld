print("Hello!")

program_choice = 0
while(program_choice != 5):
  program_choice = int(input(
    " Please select a program: " +
    " 1. Food quiz "+
    " 2. Test score"+
    " 3. Did you stay in for recces"+
    " 4. What course you want to do"+
    " 5. How much kg would it be on Planets"+
    " 6. To qiut      "
  ))

  if program_choice == 1: 
    print("What food do you like?")
    x = input()
    if x.lower() == "pasta":
        print("HI PASTA LOVER!")
    else:
        print("NOOOOO WRONG ANSWER!!! DID YOU MEAN PASTA?")

  elif program_choice == 2:
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

  elif program_choice == 3:
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

  elif program_choice == 4:
    fin_lit = "Financial Literacy"
    pixar = "Pixar in a Box"
    grammar = "Grammar"

    grade = int(input("What grade are you in? "))
    favorite_subject = input("What is your favorite subject? ")
      
    rec = ""
    if grade < 6:
      rec = grammar
    else:
      if favorite_subject == "computing" or favorite_subject == "art":
        rec = pixar
      else:
        rec = fin_lit

    print("We recommend this course: " + rec)
  elif program_choice == 5:
    planet = input("Pick a planet: Mars, Mercury, Venus, or Jupiter ")

    gravity= 0.0
    if planet == "Mars" or planet == "Mercury":
      gravity = 3.7
    elif planet == "Venus":
      gravity = 3.7
    elif planet == "Venus":
      gravity = 8.9
    elif planet == "Jupiter":
      gravity = 23.1
    else:
      print("Unrecongized planet")

    if gravity:
      earth_weight = float(input("How much does it weigh on Earth (kg)?"))
      
      earth_gravity= 9.81
      mass = earth_weight / earth_gravity
      now = round(mass * gravity, 1)
      
      print("It would weigh" + str(now) + "kg on " + planet + ".")
  else :
    print("GOODBYE!!!!")
