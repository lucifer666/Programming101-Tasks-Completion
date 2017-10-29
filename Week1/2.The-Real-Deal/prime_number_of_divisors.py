from is_prime import is_prime

def prime_number_of_divisors(number):
    return is_prime(len([digit for digit in range(1, number+1) if number % digit == 0]))

print(prime_number_of_divisors(7))
print(prime_number_of_divisors(8))
print(prime_number_of_divisors(9))
