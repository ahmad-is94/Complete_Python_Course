def find_names(names,target):
    left = 0
    right = len(names)-1
    while left <= right:
        mid = (left+right)//2
        if names[mid] == target:
            return mid
        elif names[mid] < target:
            left = mid+1
        else:
            right = mid-1
            return -1


names = ['ahmad','ali','s','d','d','f','g','h','j','u','y','tt','t','t','r','y']
target = 'tt'
result = find_names(names,target)
if result !=-1:
    print(result)
else:
    print('No Name')


