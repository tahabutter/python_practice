import json

json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
data = json.loads(json_string)
print(data)
print(type(data))


pyn_obj = {"name": "Bob",
"age": 25,
"isCity": "None"}

# Convert Python dictionary to JSON string
json_str = json.dumps(pyn_obj)
print(json_str)
print(type(json_str))