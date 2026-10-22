marks = {
    'ahmad':"ali",
    "marks":90,
    "roll_no":1234
}
print(marks['marks'])


mark= {}
mark['ahmad']= "ali"
mark['marks']= 23
print(mark['marks'])


del mark['marks']
print(mark)

#check frequency of numbers in hashing
numbers=[1,2,3,4,5,5,5,6,6,7,7]
freq ={}
for i in numbers:
    freq[i]=freq.get(i,0)+1

print(freq)


nums = [4, 2, 4, 3, 2, 4]
B ={}
for i in nums:
    B[i]=B.get(i,0)+1
print(B)


