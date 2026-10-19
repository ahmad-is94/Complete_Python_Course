import numbers


def find_duplicates(numbers):
    for i  in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j and numbers[i]==numbers[j]:
                return True
    return False
numbers = [1,2,3,4,4,5,6,7,8,9]
result = find_duplicates(numbers)
if result:
    print('c')
else:
    print('d')