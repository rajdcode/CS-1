#Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
#Enter your name: Chuck
#Hello Chuck
nam = input('Enter your name\n')
print('Hello',nam)

#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
hrsworked = input('enter hours')# input deliver type of string 
a = float(hrsworked)# str to int 
print(a)
rate =input('enter rate per hour')
b=float(rate)
print(b)
Pay = a*b
print(Pay)

#Exercise 4: Assume that we execute the following assignment statements:
#width = 17
#height = 12.0
#For each of the following expressions, write the value of the expression and the type (of the value of the expression).
#width//2
width =17
mod = width//2
print(mod)# prints the value of mod
type(mod) # prints type of mod 

#width/2.0
width =17 # value is assigned to varibale width
div= width/2.0 # py3 it will display floating values
print(div)
output : 8.5
#height/3
height = 12.0
divheight = height/3
print(divheight)
>>output 4


#1 + 2 * 5

precednet = 1+(2*5)
print (precedent)
>>output :11
