person = {
    "name": "Yateng",
    "emails": ["yateng@gmail.com", "yateng@email.com", "yt@hotmail.com"],
    "address": "Brossard"
}

print(person)
print(person["name"])

for key in person:
    print(f"Person[{key}] = {person[key]}")

person["address"] = "somewhere else"
print(person)

person["id"] = 1003
print(person)

# print(person["abcde"])
print("abcd ---> ", person.get("abcd"))
print("id ---> ", person.get("id"))
print("abcd ---> ", person.get("abcd", "Key doesn't exist!"))

# A list of persons
# person_list = [person]
# print(person_list)
# person_list = [
#     {
#         "name": "Yateng",
#         "emails": ["yateng@gmail.com", "yateng@email.com", "yt@hotmail.com"],
#         "address": "Brossard"
#     },
#     {
#         "name": "Remy",
#         "emails": ["re@gmail.com", "ey@email.com", "ra@hotmail.com"],
#         "address": "Laval"
#     }
# ]
#
# # person_list.append(person)
# print(person_list)

names = ['yateng', 'dennis', 'Bob']
person2 = {name: name.upper() for name in names}
print(person2)
print(person2.keys())
person3 = {key: "test" for key in person}
print(person3)


def get_data(key):
    return key.upper()


person4 = {key: get_data(key) for key in person}
print(person4)
