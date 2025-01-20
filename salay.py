import json
data = {"1":"amruta", "2":"Abhi"}
print(json.dumps(data))


json_data = '{"name":"Amruta", "age":25}'
print(json.loads(json_data))