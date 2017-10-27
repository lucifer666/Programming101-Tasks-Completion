def contains_digits(number, digits):
    return digits == [digit for digit in digits if str(digit) in str(number)]

print(contains_digits(402123, [0, 3, 4]))
print(contains_digits(666, [6,4]))
print(contains_digits(123456789, [1,2,3,0]))
print(contains_digits(456, []))