Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F
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
hours = input('enter hours')
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

#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6    F
 
 grade = input ('enter grade')
 fgrade = float(grade)
 print (fgrade)
 if fgrade>0.0 and fgrade<1.0 and fgrade>=0.9 :
       print('grade is A')
    elif fgrade>=0.8 :
              print('grade is B')
    elif fgrade>=0.7 :
              print('grade is C')
    elif fgrade>=0.6 :
              print('grade is D')
    elif fgrad<=0.6 :
              print('grade is F') 
     else :
        print('Bad score')
  
