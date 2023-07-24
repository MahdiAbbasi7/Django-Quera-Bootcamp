# A program’s control flow is the order in which the program’s code executes.
# we have tree models of control structure in python  : 1-Sequential, 2-Selection/Decision, 3-Repetition.

## This is a Sequential statement
 
a=20
b=10
c=a + b
print("Subtraction is : ",c)

## This is Selections statement , Some selcetion statement are  : _if _if-else _nested-if _if-elif-else 
# if example
 
input = int(input())

if input == 1 :
    print("the input number is 1")


# if-else example : 

if input % 2 == 0 :
    print("the input number is even")
else : 
    print("the input number is odd")

#  nested if example : 
a1 = 20
b1 = 10
c1 = 15
if a1 > b1:
   if a1 > c1:
      print("a1 value is big")
   else:
       print("c1 value is big")
elif b1 > c1:
    print("b1 value is big")
else:
     print("c1 is big")

# if_elif_else example
x = 100
y = 50

if x > y :
    print("x value is bigger than y value") 
elif x == y :
    print(" both is equal")
else : 
    print("y is bigger than x value")


# This is a Repetition statements that divide to _for and _while loops 
# for 

print("first example")

lst = [1,2,3]
for i in  range(len(lst)):
    print(" i in list is :" + str(lst[i]))

print("sconde example")
for j in range(0,5):
    print(j)

# while 
print("while example is :")
m = 5
i1 = 0
while i1 < m:
     print(i1, end = " ")
     i1 = i1 + 1
print("End")

# this is example for shorthand of if and else 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

