import json

with open('sampleJson.json') as f:
    data = json.load(f)

    with open('newSample.json', 'w') as newFile:
        json.dump(data, newFile, indent=2)
        # newFile.write(jsonData)