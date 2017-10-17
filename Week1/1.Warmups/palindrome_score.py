def p_score(number):
    p_score = 1
    number_str = str(number)
    is_palindrome = False
    if number_str != number_str[::-1]:
        while(is_palindrome != True):
            number += int(str(number)[::-1])
            number_str = str(number)
            p_score += 1
            if number_str == number_str[::-1]:
                is_palindrome = True
                break
    return p_score

print(p_score(121))
print(p_score(48))
print(p_score(198))
