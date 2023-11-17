# sort a list of dictionaries using Lambda based on color.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
#  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
#  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
#  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, 
#  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

d = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

d.sort(key=lambda x: x['color'])
print(d)