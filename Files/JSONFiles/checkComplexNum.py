data = '''
{"__complex__": true, "real": 4, "img": 5}
'''
import json

def checkComplex(obj):
    if '__complex__' in obj:
        return f"{obj['real']} + {obj['img']}j"


pyData = json.loads(data, object_hook=checkComplex)
print(type(pyData))

print(pyData)
