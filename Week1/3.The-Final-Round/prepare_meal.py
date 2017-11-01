def prepare_meal(number):
    spam, eggs = "",""
    num = number
    while(num % 3 == 0):
        if num % 3 == 0:
            num /= 3
            spam += "spam "
    if number % 5 == 0:
        eggs = "eggs"
    if spam and eggs:
        return spam + " and " + eggs
    elif not spam and not eggs:
        return "''"
    return spam + eggs

print(prepare_meal(5))
print(prepare_meal(3))
print(prepare_meal(27))
print(prepare_meal(15))
print(prepare_meal(45))
print(prepare_meal(7))

