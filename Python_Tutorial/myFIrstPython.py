age = 18
weight = 75.5
print('今年は%d歳です' % age)
print('私の体重は%.2fkgです' % weight)
print('今年は%d歳で、体重は%.2fkgです。来年は%d歳です' % (age, weight, age + 1))
print('今年は%s歳で、体重は%skgです。来年は%s歳です' % (age, weight, age + 1))
print(f'今年は{age}歳で、体重は{weight}です。来年は{age+1}歳です')

print('hello', end="\n")
print('world', end="\t")
print('test', end="...")