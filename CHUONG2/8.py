import json
data={
    "name":"A",
    "age":35,
    "company":"Đất Việt"
}
json_string=json.dumps(data, ensure_ascii=False)
print(json_string)
print(type(json_string))