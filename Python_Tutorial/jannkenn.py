import random

player = int(input('0 --- stone, 1 --- scissor, 2 --- cloth\n'))
computer = random.randint(0, 2)
print(f'Computer choose: {computer}')

if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('You Win!')
elif player == computer:
    print('Draw')
else:
    print('Computer Wins!')