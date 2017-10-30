#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
hours worked = input('enter hours)
hrsworked = float('hours worked')
if(hrsworked<=40):
  print('Entered hours are less than 40, normal rate applies)
  Pay = hrsworked*10
  print(Pay)
elif(hrsworked>40):
  Print('Entered hours are greater than 40, penality rate applies for extra hours)
  Pay = hrsworked*10+(hrsworked-40)*10*1.5
  print(Pay)
  
#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input
hours = input('enter hours)
rate = input('enter rate')
try:
    hrs = int(hours)
    print('hrs')
    rte = int(rate)
    print('rte')
    Pay = hrs*rte
    print(Pay)
except:
      print('Error, please enter numeric input')
