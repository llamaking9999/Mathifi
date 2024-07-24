#copy all of this by doing Control-A then Control-C
#mathtime!
#version 1.1

import random

score = 0
loop = 0
the_x_factor = 0
divnum1 = 0
divnum2 = 0
inputed_answer = 1
correct_answer = 1
Hard_mode = input("hard mode?(yes or no)")
OP = input("what operation?(like +, -, *, /)")
for _loop in range (1,10):
  the_x_factor = 0
  divnum1 = 0
  divnum2 = 0
  if Hard_mode == "yes":
    num1 = random.randint(6,24)
    num2 = random.randint(6,24)
    the_x_factor = random.randint(1,8)
    for _normaly in range (6,(random.randint(12,24))):
      divnum1 += 2
    divnum2 = divnum1*the_x_factor
  else:
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    the_x_factor = random.randint(1,6)
    for _normaly in range (1,(random.randint(3,6))):
      divnum1 += 2 
  divnum2 = divnum1*the_x_factor
  print("")
  if OP == ("+"):
      correct_answer = num1 + num2
      inputed_answer = input("what is " + str(num1) + "+" + str(num2) + "?")
      print("what is " + str(num1) + "+" + str(num2) + "?")
      inputed_answer = int(inputed_answer)
      print(inputed_answer)
      if inputed_answer == correct_answer:
        print("correct")
        if Hard_mode == "yes":
          score += 2
        else:
          score += 1
      else:
        print("wrong, the correct answer is", str(correct_answer))

  if OP == ("-"):
    if num1 > num2:
      correct_answer = num1 - num2
      inputed_answer = input("what is " + str(num1) + "-" + str(num2) + "?")
      print("what is " + str(num1) + "-" + str(num2) + "?")
    else:
      correct_answer = num2 - num1
      inputed_answer = input("what is " + str(num2) + "-" + str(num1) + "?")
      print("what is " + str(num2) + "-" + str(num1) + "?")
    inputed_answer = int(inputed_answer)
    print(inputed_answer)
    if inputed_answer == correct_answer:
      print("correct")
      if Hard_mode == "yes":
        score += 3
      else:
        score += 2
    else:
      print("wrong, the correct answer is", str(correct_answer))

  if OP == ("*"):
    correct_answer = num1 * num2
    inputed_answer = input("what is " + str(num1) + "*" + str(num2) + "?")
    print("what is " + str(num1) + "*" + str(num2) + "?")
    inputed_answer = int(inputed_answer)
    print(inputed_answer)
    if inputed_answer == correct_answer:
      print("correct")
      if Hard_mode == "yes":
        score += 4
      else:
        score += 3
    else:
      print("wrong, the correct answer is", str(correct_answer))
  if OP == ("/"):
    if divnum1 > divnum2:
      correct_answer = divnum1 / divnum2
    else:
      correct_answer = divnum2 / divnum1
    if divnum1 > divnum2:  
      inputed_answer = input("what is " + str(divnum1) + "/" + str(divnum2) + "?")
      print("what is " + str(divnum1) + "+" + str(divnum2) + "?")
    else:
      inputed_answer = input("what is " + str(divnum2) + "/" + str(divnum1) + "?")
      print("what is " + str(divnum2) + "/" + str(divnum1) + "?")
    inputed_answer = int(inputed_answer)
    print(inputed_answer)
    if inputed_answer == (correct_answer):
      print("correct")
      if Hard_mode == "yes":
        score += 5
      else:
        score += 4
    else:
      correct_answer = int(correct_answer)
      print("wrong, the correct answer is", str(correct_answer))
      
  if OP != ("+") and OP != ("-") and OP != ("*") and OP != ("/"):
    print("bruh, thats not an operation")
score = int(score)
print("your score is",score)
if score > 44:
  print("you are a math genius and literaly got the max score possible, congrats!")
if score > 20 and score < 30:
  print("meh score")
if score > 15 and score < 20:
    print("you have some potenial to be a math genius you just need to try harder")
if score < 1:
  print("wow, u got everything wrong, how did you do that?")
if score > 30 and score < 45:
  print("you did pretty good")
if score > 0 and score < 15:
  print("you did not too good...")































  

