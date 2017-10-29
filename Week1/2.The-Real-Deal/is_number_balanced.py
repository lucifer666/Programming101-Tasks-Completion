def is_number_balanced(number):
    if number in range(0,10):
        return True
    numbers_list = [int(num) for num in str(number)]
    middle = len(numbers_list)/2
    if len(str(number)) % 2 == 0:
        return sum(numbers_list[:middle]) == sum(numbers_list[middle:])
    else:
        return sum(numbers_list[:middle]) == sum(numbers_list[middle+1:])

print(is_number_balanced(9))
print(is_number_balanced(11))
print(is_number_balanced(13))
print(is_number_balanced(121))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))