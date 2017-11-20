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

def goldbach(number):
    primes_less_than_number = [num for num in range(2, number) if is_prime(num)]
    combination_list = []
    for current_num1 in primes_less_than_number:
        for current_num2 in primes_less_than_number:
            if (current_num1 + current_num2 == number) and current_num1 <= current_num2:
                combination_list.append((current_num1, current_num2))
    return combination_list

print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
