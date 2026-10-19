def find_two_numbers(num1,target):
    left = 0
    right = len(num1)-1
    while left < right:
        total = num1[left] + num1[right]
        if total == target:
            return num1[left]
        elif total > target:
            right -= 1
        else:
            left += 1
            return []
numbers = [1,2,3,4,555,55,6,7,8]
print(find_two_numbers(numbers,55))
