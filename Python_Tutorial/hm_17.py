t1 = (10, 20, 30)
# In tuple it needs to add a comma even though there is only 1 data,
# otherwise it will be other data type.
t2 = (10, 'bb', [10, 'yy'])

print(t1[0])
print(t1.index(20))
print(t1.count(30))
print(len(t1))
# t1[0] = 'aa' error
# The modification in below is valid.
# Because the array in tuple can be modified directly
t2[2][0] = 20
print(t2)