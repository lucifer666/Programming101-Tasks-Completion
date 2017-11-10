#refactoring needed

from group import group

def max_consecutive(items):
    longest_subsequence = 0
    for index, item in enumerate(group(items)):
        if index == 0:
            longest_subsequence = len(item)
        elif len(item) > longest_subsequence:
            longest_subsequence = len(item)
    return longest_subsequence

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
