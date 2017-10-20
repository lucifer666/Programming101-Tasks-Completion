from palindrome import palindrome

def p_score(number):
    p_score = 1
    if not palindrome(number):
        while(True):
            number += int(str(number)[::-1])
            p_score += 1
            if palindrome(number):
                break
    return p_score

print(p_score(121))
print(p_score(48))
print(p_score(198))
