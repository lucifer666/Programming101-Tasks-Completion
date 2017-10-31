def zero_insert(number):
    number_list = [int(digit) for digit in str(number)]
    item_index = 1
    while(True):
        if item_index >= len(number_list):
            break
        if number_list[item_index - 1] == number_list[item_index]:
            number_list.insert(item_index, 0)
        elif (number_list[item_index-1] + number_list[item_index]) % 10 == 0:
            number_list.insert(item_index, 0)
        item_index += 1
    return "".join([str(number) for number in number_list])

print(zero_insert(116457))
print(zero_insert(55555555))
print(zero_insert(1))
print(zero_insert(6446))
