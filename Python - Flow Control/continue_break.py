# The continue break statement 
    
# The break statement terminates the current loop and resumes the execution at the next statement (just like in C).

aString = 'I Love Python Programming'
print('The Full Statement: ', aString)

for i in aString:
    if i == 'm':
        break
    print(i)

print('\n')
print('Finished.')

# The continue statement in Python returns the control to the beginning of the while loop.

var = 5

while var > 0:
    var = var - 1
    if var == 2:
        continue
    print('Variable: ',var)

print('\n')
print('Finished')

