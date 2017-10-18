def is_increasing(seq):
    if len(seq) == 1:
        return True
    for index in range(0, len(seq)-1):
        if seq[index] >= seq[index+1]:
            return False
    return True



print(is_increasing([1,2,3,4,5]))
print(is_increasing([1]))
print(is_increasing([5,6,-10]))
print(is_increasing([1,1,1,1]))

