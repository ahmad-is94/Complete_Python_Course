"""using continue statement with loops
#for i in range(1,11):
 #   if i%2 ==0:
        continue
    print(i)/*
#Skipping Specific Values
for char in "python programming":
    if char =="o":
        continue
    print(char,end=" ")

##text = "python programming"
#i = 0
#while i < len(text):
 #   T1 = text[i]
   # if T1 =="o":
  #   i += 1
    # continue
    #print(T1,end=" ")

#i += 1"""
''''x = 0 
while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)'''''

'''list = [1,2,-2,-4]
for i in list:
    if i < 0 :
        continue
    print(i)'''''
    
'''list1  = [1,2,3,4,-6]
i = 0
while i < len(list1):
    if list1[i] < 0:
        i += 1
        continue
    print(i,end=" ")
    i += 1'''''
'''sentence = "My name is ali "
skip = ['is','ali']
for word in sentence.split():
    if word in skip:
        continue
    print(word,end=" ")'''
#skipSkipping Multiples of 3 in a Range
for i in  range(1,38):
    if i % 3 ==0:
        continue
    print(i)
