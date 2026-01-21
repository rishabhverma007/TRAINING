adict = {"Name":"Rishabh Verma",
         "Section":"CSE-AI 3D",
         "Roll No":1230439243}
print(adict)
data = {"a":1,"a":2}
print(data)
students = [{"name":"Amit","marks":80},
            {"name":"Ravi","marks":45},
            {"name":"Neha","marks":95}]
for s in students:
    if s["marks"]>=60:
        print(s["name"])


self_care_products = {"brand":"dermaco","hair_care":"minoxidil"}
print(list(self_care_products.keys())[0])
