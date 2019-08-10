# The for loop.

listOne = [
    1,2,3,4,5,6,7,8,9,10
]

totalSum = 0

for i in listOne:
    totalSum += i

print('The List: ',listOne)

print('Their total: ', totalSum)
print('----------------------------------------------------------------')

# The range function in for loop. 
# A range is a function that returns a sequence of number starting from 0 and is incremented by 1 and ends at a specified number.

x = range(7)

for i in x:
    print(i)
    
print('----------------------------------------------------------------')

# A python program to iterate through a list using range and indexing. 

aList = [
    'Computer Science', 'Programming', 'Python' 
]

for var in range(len(aList)):
    print('I love ', aList[var])

print('----------------------------------------------------------------')

# The for-else loop. 

anotherList = [
    1, 3, 5, 7, 9, 11
]

for variables in anotherList:
    print('The numbers are: ', variables)
else:
    print('\n')
    print('All numbers are displayed. None exist in the list.')
