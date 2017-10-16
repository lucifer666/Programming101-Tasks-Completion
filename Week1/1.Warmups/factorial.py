def factorial(number):
    if number in [0,1]:
    	return number
    return number * factorial(number-1) 

print(factorial(0))
print(factorial(1))
print(factorial(5))