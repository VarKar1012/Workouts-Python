jdata = '''
{
    "people":[
        {
        "name":"devin",
        "phone":1234567899,
        "email":"devin@gmail.com",
        "has_licence": true 
        },   
        {
        "name":"dainty",
        "phone":1234444444,
        "email":null,
        "has_licence": false    
        }
        
    ]
}
''' #docstring
import json

data = json.loads(jdata) # to load a json data / doc string
# print(data)
# {'people': [
# {'name': 'devin', 'phone': 1234567899, 'email': 'devin@gmail.com', 'has_licence': True}, 
# {'name': 'dainty', 'phone': 1234444444, 'email': None,  'has_licence': False}
# ]}
print(type(data)) #<class 'dict'>

# for i in data['people']:
#     # print(i)
#     # {'name': 'devin', 'phone': 1234567899, 'email': 'devin@gmail.com', 'has_licence': True}
#     # {'name': 'dainty', 'phone': 1234444444, 'email': None, 'has_licence': False}

#     print(i['name']) #devin dainty

# data = json.loads(jdata)
# for i in data['people']:
#     del i['phone']

# print(data)
# print(type(data)) #<class 'dict'>
# # {'people': [{'name': 'devin', 'email': 'devin@gmail.com', 'has_licence': True}, 
# # {'name': 'dainty', 'email': None, 'has_licence': False}]}

# newData = json.dumps(data)
# print(newData)
# # {"people": [{"name": "devin", "email": "devin@gmail.com", "has_licence": true}, 
# # {"name": "dainty", "email": null, "has_licence": false}]}
# print(type(newData)) #<class 'str'>

# newData = json.dumps(data, indent=2) # to get data in json format
# print(type(newData)) #str
# print(newData)
# {
#   "people": [
#     {
#       "name": "devin",
#       "email": "devin@gmail.com",
#       "has_licence": true
#     },
#     {
#       "name": "dainty",
#       "email": null,
#       "has_licence": false
#     }
#   ]

# newData = json.dumps(data, sort_keys=True)
# print(newData) 
# # {"people": [{"email": "devin@gmail.com", "has_licence": true, "name": "devin"}, 
# # {"email": null, "has_licence": false, "name": "dainty"}]}
# -----------------------------------------------------------

# To load a json file in python

# with open('states.json') as f:
#     data = json.load(f)
#     print(data)
    # {'states': [{'name': 'Alabama', 'abbreviation': 'AL', 'areacode': ['123', '205', '455']}, 
    # {'name': 'Alaska', 'abbreviation': 'AK', 'areacode': ['233']},
    #  {'name': 'American Samoa', 'abbreviation': 'AS', 'areacode': ['234', '566']}, 
    # {'name': 'Arizona', 'abbreviation': 'AZ', 'areacode': ['239', '567', '888']}, 
    # {'name': 'Arkansas', 'abbreviation': 'AR', 'areacode': ['345', '457']},
    #  {'name': 'California', 'abbreviation': 'CA', 'areacode': ['444']}, 
    # {'name': 'Colorado', 'abbreviation': 'CO', 'areacode': ['777']}, 
    # {'name': 'Connecticut', 'abbreviation': 'CT', 'areacode': ['345', '898']}, 
    # {'name': 'Delaware', 'abbreviation': 'DE', 'areacode': ['067']}, 
    # {'name': 'District Of Columbia', 'abbreviation': 'DC', 'areacode': ['234', '456']}]}

# with open('states.json') as f:
#     data = json.load(f)

#     with open('newStates.json', 'w') as newFile:
#         # json.dump(data, newFile) #writes the data in single line
#         json.dump(data, newFile, indent=2) #writes the data in json format
# ----------------------------------------------
# with open('states.json') as f:
#     data = json.load(f)

#     for i in data['states ']:
#         del i['areacode']

#     with open('newStates1.json', 'w') as newFile:
#         # json.dump(data, newFile) #writes the data in single line
#         json.dump(data, newFile, indent=2) #writes the data in json format

# ------------------------------------------------
# to read / write json data from a URL

import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(response) # http-200 status
# print(response.text) #gives content

data = json.loads(response.text) # loads used, bcoz response.text is a string
with open('urlWrite1.json', 'w') as f:
    json.dump(data, f, indent=2)

with open('urlWrite2.json', 'w') as f:
    json.dump(response.json(), f, indent=2)

