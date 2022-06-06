index = 0

while index < 100:
    print('HELLO!')
    index+=1

print('FINISH')

i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1

print(f'Result 1: {result}')

i = 0
result = 0
while i <= 100:
    result += i
    i += 2

print(f'Result 2: {result}')