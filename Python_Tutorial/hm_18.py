dict1 = {'name': 'Tom', 'age': 20, 'gender': '男性'}
dict2 = {}
dict3 = dict()

dict1['name'] = 'Amy'
dict1['id'] = 110
print(dict1)

# del dict1['gender']
# print(dict1)

# dict1.clear()
# print(dict1)

# print(dict1.get('age'))
# print(dict1.get('id2', 999))  # If id2 does not exist, print 999
# print(dict1.keys())
# print(dict1.values())

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for item in dict1.items():
    print(item)

for key, value in dict1.items():
    print(f'{key} = {value}')