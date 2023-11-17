# Parse the following JSON to get all the values of a key ‘name’ within an array

jsonData = '''
[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]'''

import json

pyData = json.loads(jsonData) #py data

# name = [value for i in pyData for key, value in i.items() if key == 'name']
name = [i['name'] for i in pyData]
print(name)