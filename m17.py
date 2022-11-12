with open('C://py_ege//17.txt', 'r') as f:
    nums = [int(i) for i in f]
    max_elem = max([i ** 2 for i in nums if abs(i) % 10 == 3])

count = []

for n in range(1, len(nums)):
    n1 = abs(nums[n - 1]) % 10
    n2 = abs(nums[n]) % 10

    if (n1 == 3 and n2 != 3) or (n2 == 3 and n1 != 3):
        if (nums[n - 1] ** 2 + nums[n] ** 2) >= max_elem:
            count.append(nums[n - 1] ** 2 + nums[n] ** 2)

print(len(count), max(count))