def find_max(numbers, function):
    maximum = numbers[0]
    for x in numbers:
        maximum = function(maximum, x)
    return maximum

num = [7, 5, 6, 10, 4, 2, 9, 0]
f = lambda x, y: x if x > y else y

print(find_max(num, f))