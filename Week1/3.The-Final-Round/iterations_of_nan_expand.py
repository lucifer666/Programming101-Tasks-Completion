#refactoring needed
def iterations_of_nan_expand(expanded):
    if not expanded:
        return 0
    expanded_list = [item.strip() for item in expanded.split("Not a") if item != " "]
    for word in expanded_list:
        if word not in ["", "NaN"]:
            return False
    return expanded.count("Not a")

print(iterations_of_nan_expand(""))
print(iterations_of_nan_expand("Not a NaN"))
print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print(iterations_of_nan_expand("Show these people!"))
