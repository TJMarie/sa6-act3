num = 1234
nums = []
digits = len(str(num))

for i in range(digits):
    nums.append(num % 10)
    num = num // 10

print(sum(list(filter(lambda x: (x), nums))))