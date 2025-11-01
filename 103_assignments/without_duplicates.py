def without_duplicates(values):
    new_list = []
    for item in values:
        if item not in new_list:
            new_list.append(item)
    return new_list
my_list = [3, 4, "candy", 9878, 4, 8]
result = without_duplicates(my_list)
print(result)