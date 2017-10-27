def is_number_balanced(number):
    if len(str(number)) == 1:
        return True
    if len(str(number)) % 2 == 0:
        numbers_list = [int(num) for num in str(number)]
        middle = int(len(str(number))/2)
        return sum(numbers_list[:middle]) == sum(numbers_list[middle:])
    else:
        numbers_list = [int(num) for num in str(number)]
        middle = int(len(str(number)) / 2)
        return sum(numbers_list[:middle]) == sum(numbers_list[middle+1:])


print(is_number_balanced(9))
print(is_number_balanced(11))
print(is_number_balanced(13))
print(is_number_balanced(121))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))