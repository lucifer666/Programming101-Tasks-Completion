#need to be improved

import math

def is_prime(number):
    if number < 2:
        return False
    divider = 2
    max_divider = math.sqrt(number)
    while(divider <= max_divider):
        if number % divider == 0:
            return False
        divider += 1
    return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(8))
print(is_prime(11))
print(is_prime(-10))
