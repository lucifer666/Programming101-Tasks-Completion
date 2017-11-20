#refactoring needed

def is_credit_card_valid(number):
    digits_list = [int(digit) for digit in str(number)]
    transformed_digits_list = [digit*2 if index % 2 != 0 else digit for index, digit in enumerate(digits_list)]
    sum_digits_in_trans_number = sum([int(digit) for digit in "".join([str(number) for number in transformed_digits_list])])
    return sum_digits_in_trans_number % 10 == 0 and len(digits_list) % 2 != 0

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
