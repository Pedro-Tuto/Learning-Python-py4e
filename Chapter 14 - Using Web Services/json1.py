import json
data = '''{
    "name" : "Gabigolmes",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "sim"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide', info["email"]["hide"])

