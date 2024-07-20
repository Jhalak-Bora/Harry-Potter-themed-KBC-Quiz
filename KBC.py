print("\n Welcome to Harry Potter Quiz. All the best! \n\n Rules to keep in mind: \n\n 1. Wrong answer after 5th question will drop you to 10000\n 2. Wrong answer after 10th question will drop you to 320000\n 3. Quitting the quiz will give the money you've earned so far")

a = input("Would you like to proceed?")
    
        
questions = [
  [
    "What house does Luna Lovegood belong to??", "Gryffindor", "Slytherin", "Ravenclaw",
    "Hufflepuff", 3
  ],
  [
    "What is Harry’s Patronus?", "Stag", "Eagle", "Rabbit",
    "Horse", 1
  ],
  [
    "Who guards the entrance to the Gryffindor common room?", "Soldier", "Fat Lady", "Prefect",
    "Gargoyle", 2
  ],
  [
    "Who played Ron Weasely?", "Rupert Grint", "Danielle Radcliffe", "Robert Pattinson",
    "RDJ", 1
  ],
  [
    "Where do Hogwarts students buy their wands?", "Gringotts", "Hogsmeade", "Diagon Alley",
    "Ollivanders'", 4
  ],
  [
    "How many Horcruxes did Voldemort create intentionally?", "5", "6", "7",
    "8", 2
  ],
  [
    "What is the name of the magical creature that can only be seen by those who have witnessed death?", "Dragon", "Phoenix", "Thestral",
    "Buckbeak", 3
  ],
  [
    "Who is NOT in Gryffindor?", "Cedric Diggory", "Percy Weasley", "Neville Longbottom",
    "Ginny Weasley", 1
  ],
  [
    "What year was The Goblet of Fire published?", "2000", "2001", "2002",
    "2003", 1
  ],
  [
    "Who is the Slytherin ghost?", "Peeves", "Sir Nicholas", "Helga",
    "The Bloody Baron", 4
  ],
  [
    "What is Ron famously afraid of?", "Snakes", "Dark", "Spiders",
    "Hermoine", 3
  ],
  [
    "What’s the name of Hagrid’s half-brother?", "Grawp", "Hargrid", "Greup",
    "Tonks", 1
  ],
  [
    "Who sent Harry his Firebolt?", "Albus Dumbledore", "Sirius Black", "Remus Lupin",
    "Severus Snape", 2
  ],
  [
    "What magazine does Xenophilius Lovegood publish?", "The Scribbler", "The Dribbler", "The Quibbler",
    "The Deathly Hallows", 3
  ],
  [
    "Who refereed the Quidditch World Cup Final in 1994 between Bulgaria and Ireland?", "Herman Junker", "Nugent Potts", "Severus Snape",
    "Hassan Mostafa", 4
  ],
  
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 125000, 2500000, 500000, 10000000, 70000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\n Question for Rs. {levels[i]}")
  print(question[0])
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 3):
      money = 10000
    elif(i == 8):
      money = 320000
    elif(i == 13):
      money = 10000000
    elif(i == 14):
      money = 70000000  
    
  else:
    print("Wrong answer!")
    break 

print(f"Congratulations you're going home with Rs {money}")