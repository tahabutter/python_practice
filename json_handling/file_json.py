import json

with open('app.json', 'r') as file:
    data = json.load(file)
    print(data)


data = {"name": "Charlie",
"age": 28,
"isCity": "None"
    }

with open('app.json', 'w') as file:
    json.dump(data, file, indent=4,sort_keys=True)