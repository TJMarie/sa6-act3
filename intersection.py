list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 4, 5, 6]

print(list(filter(lambda x: x in list2, list1)))