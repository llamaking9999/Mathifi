#ver 2.2 did not take 7 years lol
import random


debug = None
correct_awnswer = 123456790
score = 0


#rules
print("Welcome to the math game!")
inputgarbage = input("these are the rules hit enter to continue ")
if inputgarbage == "sand":
  debug = input("debug mode activated")
  print()
  print("1 to make question one multiplycation")
  print("2 for version info")
  print()
  debug = input("what do you want to do?")
  debug = int(debug)
  if debug == 2:
    print()
    print("version 2.2")
    inputgarbage = input
   
print()
scoreinputgarbage = input(
    "you will have to answer word problems until you get one wrong, "
    "then you will get your score"
)
print()


inputgarbage = input(
    "multiplying is weird, if its starting as 7 and then it does a multiplied by 1 "
    "the total will be 14"
)
print()
inputgarbage = input("that's beacuase that's how many MORE you found")
for _meme in range(1,7):
  print()


inputed_thingy = correct_awnswer
while inputed_thingy == correct_awnswer:
  #make name 1
  names = ["James","tom","Josh","Tim","Sal","minsung","sean", "alejandro","zoe","sally"]
  name1 = random.choice(names)
  #make item 1
  items = ["friend", "enimie", "bread", "dollar", "quantom-computers"]
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
  num8 = random.randint(1,12)
  num9 = random.randint(1,12)
  num99 = random.randint(1,12)
  num999 = random.randint(1,12)
  num10 = random.randint(2,7)
  numy = random.randint(1,320)
  nummy = random.randint(1,320)


  #operation parts                                                  
  op1 = random.randint(1,3)


  op2 = random.randint(1,2)


  op3 = random.randint(1,2)


  if debug == 1:
    op1 = 3


  startingnum1 = random.randint(2, 10) if op1 == 3 else random.randint(12, 700)


  correct_awnswer = startingnum1




  #starter
  print(name1, "has", startingnum1, item1 + ("s"))


    #the hard part
  if op1 == 1:
    print("first,",name1, "finds", (num1), "more", item1 + "s")
    correct_awnswer += num1
  if op1 == 2:
      while startingnum1 < num3:
        num3 = random.randint(1,320)
      print("then,",name1, "loses", num3, "more", item1 + "s")
      correct_awnswer -= num3
  if op1 == 3:
      print("one day,",(name1),"finds",(num10),"times their previous number of",(item1)+"s")
      tape = (correct_awnswer)*(num10)
      correct_awnswer += tape
  #here we go again...
  if op2 == 1:
    print("then,",name1, "finds", (num2), "more", item1 + "s")
    correct_awnswer += num2


  else:
    if op2 == 2:
      while correct_awnswer < num4:
        num4 = random.randint(1,320)
      print("next,",name1, "loses", num4, "more", item1 + "s")
      correct_awnswer -= num4
    if op2 == 3:
      print("then",(name1),"finds",(num8),"times their previous amount of",(item1)+"s")
      tape = (correct_awnswer)*(num8)
      correct_awnswer += tape


  #here we go again...
  if op3 == 1:
    print("then,",name1, "finds", (num5), "more", item1 + "s")
    correct_awnswer += num5


  else:
    if op3 == 2:
      while correct_awnswer < num6:
        num6 = random.randint(1,320)
      print("Finaly,",name1, "loses", num6, "more", item1 + "s")
      correct_awnswer -= num6
    if op3 == 3:
      print("lastly",(name1),"finds",(num9),"times their previous amount of",(item1)+"s")
      tape = (correct_awnswer)*(num9)
      correct_awnswer += tape
     


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







