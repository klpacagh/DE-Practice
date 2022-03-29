# process of opening each new box is the same
# each time we open a box, we make the problem smaller
# pseudo of open box
# keep running instance of open_box until we get a ball
# ball is the base case
'''
def open_box():
    if ball:
        return ball
    open_box()
'''

'''
Look at general call stack first
def funcThree():
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')

funcOne()

'''
# Factorial Example
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

'''
How the call stack looks:

return 1 
return 2 * factorial(1)
return 3 * factorial(2)
return 4 * factorial(3)
factorial (5) 

--> 1*2*3*4*5 = 120
'''
print(factorial(5)) 