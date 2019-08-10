# The if-else statement.

numOne = int(input('Enter an integer value in the range of 0-30: '))

if numOne > 30:
    print('The number is greater than 30.')

elif numOne > 10 and numOne < 30:
    print('The number is greater than 10 but lesser than 30.')

else:
    print('The number is lesser than 10')


# A simple program to check whether a number is zero, positive or a negative number.

ourNumber = int(input("Enter any number (positive or negative): "))

if ourNumber >= 0:
    if ourNumber == 0:
        print("The number is a zero.")
    
    else: 
        print('The number is a positive number.')

else:
    print('The number is a negative.')
