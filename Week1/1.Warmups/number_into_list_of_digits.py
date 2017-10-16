def to_digits(number):
    list_of_digits = []
    while(number != 0):
    	list_of_digits = (number % 10) + list_of_digits
    	number = number % 10
    return list_of_digits

print(to_digits(123))
print(to_digits(99999))
print(to_digits(123023))
