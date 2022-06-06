j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{j} * {i} = {i * j}', end=' \t')
        i += 1
    print()
    j += 1

str = 'inplace'
for i in str:
    if i == 'p':
        continue
    if i == 'e':
        break
    print(i)

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print('test 11')
    i+=1
else:
    print('end of test 11')

str2 = 'itheima'
for i2 in str2:
    if i2 == 'e':
        continue
    print(i2)
else:
    print('i2 ends')