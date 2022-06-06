a = 'hello ' \
    'world'
print(a)
print(type(a))

b = "TOM"
print(type(b))

e = '''i am Tom'''
print(type(e))

f = """I
am Tom"""
print(type(f))
print(f)

c = "Tom"
print(type(c))
print(c)
print("My name is %s" % c)
print(f"My name is {c}")
print(c[0])

name = input('Please enter your name: ')
print(f'You name is {name}')
print(type(name))

password = input('Please enter your password: ')
print(f'You password is {password}')
print(type(password))