import json
a = (10,20,30,40,50,60,70)
print(type(a))
b = json.dumps(a)
print(type(json.loads(b)))


load() Method

import json

student = {
    "Name": "Peter",
    "Roll-no": "0090014",
    "Grade": "A",
    "Age": 20,
}

with open("Student.json", "w") as json_file:
    json.dump(student, json_file)

with open("Student.json", "r") as json_file:
    s = json.load(json_file)
print(s)
