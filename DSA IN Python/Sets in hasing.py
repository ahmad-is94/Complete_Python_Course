nums = [1, 3, 5, 3, 7, 1]

seen = set()

for num in nums:
    if num in seen:
        print("Duplicate found:", num)
        break
    seen.add(num)



#Two sums
nums = [2, 7, 11, 15]
target = 9

seen = {}

for num in nums:
    complement = target - num

    if complement in seen:
        print(seen[complement], num)
        break

    seen[num] = True

    nums = [10, 20, 30, 40, 50]
    sn = set(nums)

    print(30 in sn)

    nums = [1, 2, 2, 3, 3, 3]
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    print(frequency[3])

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        print([seen[complement], i])
        break

    seen[num] = i