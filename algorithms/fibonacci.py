#


from math import sqrt


#
def isPrime(a):  
    result = True 
    root = sqrt(a)
    i=2

    if a == 1:
        result = False
        
    while i <= root and result == True:
        if a%i == 0:
            result = False
        i=i+1
        
    return result

#

seedOne = 0
seedTwo = 1
interationNumber = 70
i = 0

print( seedOne )

while i < interationNumber: # 
    result = seedOne + seedTwo
    if result%15 == 0: 
        print("FizzBuzz")
    elif result%3 == 0:
        print("Buzz")
    elif result%5 == 0: 
        print("Fizz")
    elif isPrime(result) == True:
        print("BuzzFizz")
    else:
        print(result )
    seedOne = seedTwo
    seedTwo = result    
    i += 1 


