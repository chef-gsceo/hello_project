names = ['abas', 'rusya', 'piro', 'gami']

for el in names:
    print(el.title())
# print(names[0].title())
# print(names[1].title())
# print(names[2].title())
# print(names[3].title())

message = "Warning, "

for el in names:
    print(message + el.title())
# print(message, names[0].title())
# print(message, names[1].title())
# print(message, names[2].title())
# print(message, names[3].title())

message = "Warning cancel"

names.insert(0, 'nina')
names.insert(3, 'lilit')
names.append('kiki')

for el in names:
    print(message, el.title())

print("Warning again")

message = "Sorry, "

while len(names) > 2:
    popped_name = names.pop()
    print(message + popped_name.title())


message = "No warning for you, "

for el in names:
    print(message + el.title())

while len(names) > 0:
    del names[0]

print(names)