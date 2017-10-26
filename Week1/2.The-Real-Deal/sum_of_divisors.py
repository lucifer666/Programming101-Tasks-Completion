def sum_of_divisors(number):
    return sum([digit for digit in range(1, number+1) if number % digit == 0])

print(sum_of_divisors(8))
print(sum_of_divisors(7))
print(sum_of_divisors(1))
print(sum_of_divisors(1000))

