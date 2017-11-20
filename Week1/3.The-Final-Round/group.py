#refactoring needed

def group(arr):
    consecutive_list = []
    inner_list = []
    for index in range(0, len(arr)):
        if inner_list == []:
            inner_list.append(arr[index])
            continue
        if arr[index] in inner_list:
            inner_list.append(arr[index])
            if index == len(arr) -1:
                consecutive_list.append(inner_list)
        else:
            consecutive_list.append(inner_list)
            inner_list = []
            inner_list.append(arr[index])
    return consecutive_list

print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))
