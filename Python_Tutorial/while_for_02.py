i = 1
while i <= 5:
    if i == 4:
        print(f'お腹いっぱい')
        break
    print(f'{i}個目リンゴを食べました')
    i += 1

i = 1
while i <= 5:
    if i == 3:
        print(f'{i}個目リンゴに虫がいました！')
        i += 1
        continue
    print(f'{i}個目リンゴを食べました')
    i += 1
