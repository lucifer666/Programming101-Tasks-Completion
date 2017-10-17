
def is_increasing(seq):
    if len(seq) == 1:
        return True
    for index in range(0, len(seq)):
        if seq[index] > seq[index+1]:
            return False
    return True



is_increasing([1,2,3,4,5])
is_increasing([1])
is_increasing([5,6,-10])
is_increasing([1,1,1,1])

