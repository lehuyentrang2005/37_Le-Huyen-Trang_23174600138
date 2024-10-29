import json
with open('7.json', 'r', encoding='utf-8') as f:
    content=f.read()
infor=json.loads(content)
print(infor)
print(type(infor))