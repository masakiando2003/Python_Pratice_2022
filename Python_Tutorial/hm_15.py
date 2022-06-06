num_list = [1, 2, 3, 4, 5, 6, 7, 8]

num_list.reverse()
print(num_list)

num_list2 = [1, 9, 4, 6, 3, 7, 2, 5, 8]
num_list2.sort(reverse=True)
print(num_list2)

num_list3 = num_list2.copy()
print(num_list3)

i = 0
while i < len(num_list3):
    print(num_list3[i], end='')
    i += 1
else:
    print()

for j in num_list3:
    print(j, end='')  # no need to be num_list[j]