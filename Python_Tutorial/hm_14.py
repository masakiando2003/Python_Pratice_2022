name_list = ['TOM', 'Lily', 'ROSE']

print(name_list)
print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list.index('ROSE'))
print(name_list.count('ROSE'))
print(len(name_list))
print('CC' in name_list)
print('ROSE' in name_list)
print('ROSE' not in name_list)

name_list.append('MING')
name_list.extend('IVY')
name_list.extend(['IVY'])
name_list.insert(2, 'TERRY')
print(name_list)

del(name_list[2])
print(name_list)

del_name = name_list.pop(2)
print(del_name)
print(name_list)

name_list.remove('I') # Remove first matched element only
print(name_list)

name_list.reverse()
print(name_list)

name_list.clear()
print(name_list)