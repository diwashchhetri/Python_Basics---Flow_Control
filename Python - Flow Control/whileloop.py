# The while loop.
# It is used when the elements are not known exactly. 

n = int(input("Enter the range upto which you wish to calculate: "))
sum = 0
count = 1

while count <= n:
    sum += count
    count += count
    
print('The sum of all natural numbers upto the given range is: ', sum)

# The while loop with else statement. 

print('After the 10th iteration, the loop will break.')
print('\n')
c = int(input('Input: '))


while c <= 10:
    print('Iteration: ', c)
    c = c + 1

else:
    print('...................')
    print('The loop is exited.')
