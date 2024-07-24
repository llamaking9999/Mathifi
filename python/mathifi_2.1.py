#ctrl+a then ctrl+c
import random

score = 0
correct_awnswer = 9
inputed_thingy = correct_awnswer
while inputed_thingy == correct_awnswer: 
  #make name 1
  names = ["James","tom","Josh","Tim","Sal","minsung","sean", "alejandro","joe","sally"]
  name1 = random.choice(names)
  #make item 1
  items = ["friend", "enimie", "bread", "dollar", "quantum-computers"]
  item1 = random.choice(items)
  #make numbers
  num1 = random.randint(1,320)
  num2 = random.randint(1,320)
  num3 = random.randint(1,320)
  num4 = random.randint(1,320)
  num9 = random.randint(1,320)
  num5 = random.randint(1,320)
  num6 = random.randint(1,320)
  num7 = random.randint(1,320)
  numy = random.randint(1,320)
  nummy = random.randint(1,320)
  startingnum1 = random.randint(12,700)
  
  #operation parts                                                  
  op1 = random.randint(1,2)
  
  op2 = random.randint(1,2)
  
  op3 = random.randint(1,2)
  
  correct_awnswer = startingnum1
  #starter
  print(name1, "has", startingnum1, item1 + ("s"))
  
    #the hard part
  if op1 == 1:
    print("then,",name1, "finds", (num1), "more", item1 + "s")
    correct_awnswer += num1
  
  else:
    while startingnum1 < num3:
      num3 = random.randint(1,320)
    print("then,",name1, "loses", num3, "more", item1 + "s")
    correct_awnswer -= num3
  
  #here we go again...
  if op2 == 1:
    print("then,",name1, "finds", (num2), "more", item1 + "s")
    correct_awnswer += num2
  
  else:
    while correct_awnswer < num4:
      num4 = random.randint(1,320)
    print("then,",name1, "loses", num4, "more", item1 + "s")
    correct_awnswer -= num4
  
  
  #here we go again...
  if op3 == 1:
    print("then,",name1, "finds", (num5), "more", item1 + "s")
    correct_awnswer += num5
  
  else:
    while correct_awnswer < num6:
      num6 = random.randint(1,320)
    print("then,",name1, "loses", num6, "more", item1 + "s")
    correct_awnswer -= num6
  
  #its finally over!
  inputed_thingy = input("how many " + item1 + "s does " + name1 + " have now? ")
  inputed_thingy = int(inputed_thingy)
  if (inputed_thingy) == correct_awnswer:
    print("correct!")
    score += 1
  else:
    print("nope!, it was", correct_awnswer)
else:
  print("sorry, ur score is",score)


