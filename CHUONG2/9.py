import json
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "email": "alice@example.com"
}
json_data = json.dumps(data, sort_keys=True, indent=4)
print(json_data)
