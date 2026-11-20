list_val = [20, 30, 40, 25, 10]

# new_list is a set of list1
res_list = set(list_val)

# removing the maximum element
res_list.remove(max(res_list))

# printing the second largest element
print(max(res_list))  