dict = {
    "name":'ahmad ali',
    "age":20,
    "hobby":'football'
}
print(dict)
print(dict.get("name"))
print(dict["hobby"])
dict['age'] = 40
print(dict)
dict["program"] = 'AI'
print(dict)

dict_x = {  
    "name": "Sachin",   
    "age": 18,   
    "gender": "male",   
    "profession": "student",  
    "country": "India"  
    }  
po = dict_x.pop("gender")
print(po)
print(dict_x)
item = dict_x.popitem()
print(item)

dict_y = {  
    "name": "Ali",   
    "age": 18,   
    "gender": "male",   
    "profession": "student",  
    "country": "pakistan"  
    }  
dict_y["age"] = 23
print(dict_y)
#  Iterating Through a Dictionary
dict1 = {  
    "Name": "Sachin",   
    "Age": 18,   
    "Gender": "Male",   
    "Profession": "Student",  
    "Country": "India"  
    }  
print("items in dict ")
for key in dict1:
    value = dict1[key]
    print(value)
    #lenth method so we can accesss the size of our dictionary ]
    
    employees_info = {  
    "John": "Sr. Software Developer",  
    "Irfan": "UI/UX Designer",  
    "Lucy": "Human Resource Manager",  
    "Peter": "Team Lead",  
    "Johnson": "Business Developer",  
    }  
    print(len(employees_info))
    #Dictionary Membership Test
    dict2 = {  
    'fruit': 'apple',  
    'vegetable': 'onion',  
    'dry-fruit': 'resins'  
}  
    print('fruit' in dict2)