import json
from os import waitpid

person_string = '{"name": "Sema", "languages": ["Python","JavaScript"]}'
# result = person["name"]
# result = person["languages"]
# print(result)

# JSON string to Dict

# result = json.loads(person_string)
# print(result)

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])



# Dict to JSON string 
person_dict = {"name": "Sema", "languages": ["Python", "C#"]}

# result = json.dumps(person_dict)
# print(result)
# print(type(result))

with open("person.json", "w") as file:
    json.dump(person_dict, file)
    