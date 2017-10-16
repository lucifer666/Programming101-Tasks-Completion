from factorial import factorial

def fact_digits(number):
    sum = 0
    number = abs(number)
    while(number != 0):
        sum += factorial(number%10)
        number = number // 10
    return sum


print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))