#refactoring needed

def groupby(func, seq):
    some_dict = {}
    inner_list = []

    for element in seq:
        if func(element) not in some_dict:
            inner_list.append(element)
            some_dict[func(element)] = inner_list
            inner_list = []
            continue
        inner_list = some_dict[func(element)]
        inner_list.append(element)
        some_dict[func(element)] = inner_list

    return some_dict




print(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))