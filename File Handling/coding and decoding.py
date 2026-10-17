import json
# person = '{"Name": "Andrew","City":"English", "Number":90014, "Age": 23,"Subject": ["Data Structure","Computer Graphics", "Discrete mathematics"]}'
# b = json.loads(person)
# print(b)
#Encoding
s ={
    'name':'Peter',
    'grade':'A'
}
#encoding ya serialization
b = json.dumps(s)
print(b)


import json

data = '{"name": "Ali", "age": 20}'

student = json.loads(data)

print(student)
print(type(student))