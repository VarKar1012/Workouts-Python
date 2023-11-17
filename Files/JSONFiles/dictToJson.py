data = {"key1" : "value1", "key2" : "value2"}

import json

with open('dictToJson.json', 'w') as f:
    # dumpedData = json.dumps(data, indent=2)
    # f.write(dumpedData)

    dumpedData = json.dump(data, f )