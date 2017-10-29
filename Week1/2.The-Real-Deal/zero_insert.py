def zero_insert(number):
    number_list = [int(digit) for digit in str(number)]
    for index in range(1, len(number_list)):
        if number_list[index-1] == number_list[index]:
            number_list.insert(index, 0)
        elif (number_list[index-1] + number_list[index]) % 10 == 0:
            number_list.insert(index, 0)
    return "".join([str(number) for number in number_list])



print(zero_insert(116457))
print(zero_insert(55555555))
zero_insert(55555555)
# print(zero_insert(1))
# print(zero_insert(6446))
