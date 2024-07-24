import random


#make name 1
names = ["James", "tom", "Josh", "jim", "Tim"]
name1 = random.choice(names)
#make item 1
items = ["friend", "enimie", "bread", "dollar", "quantom-computers"]
item1 = random.choice(items)
#make numbers
num1 = random.randint(1,250)
num2 = random.randint(1,250)
num3 = random.randint(1,250)
num4 = random.randint(1,250)
startingnum1 = random.randint(12,450)


#operation parts
op1 = random.randint(1,2)
op2 = random.randint(1,2)




correct_awnswer = startingnum1
#starter
print(name1, "has", startingnum1, item1 + ("s"))


 #the hard part
if op1 == 1:
 print("then,",name1, "finds", (num1), "more", item1 + "s")
 correct_awnswer += num1
 if op1 == 2:
    while startingnum1 < num3:
        num3 = random.randint(1,250)
    if startingnum1 > num3:
      print("then,",name1, "loses", num3, "more", item1 + "s")
      correct_awnswer -= num3
    
#here we go again...
if op2 == 1:
 print("then,",name1, "finds", (num2), "more", item1 + "s")
 correct_awnswer += num2


if op2 == 2:
 while correct_awnswer < num4:
   num4 = random.randint(1,250)
   if correct_awnswer > num4:
     print("then,",name1, "loses", num4, "more", item1 + "s")
     correct_awnswer -= num4


#its finally over!
inputed_thingy = input("how many " + item1 + "s does " + name1 + " have now?")
inputed_thingy = int(inputed_thingy)
if (inputed_thingy) == correct_awnswer:
 print("correct")
else:
 print("nope!")








