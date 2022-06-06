import matplotlib.pyplot as pit

x_values = range(1, 6)
y_values = [x**3 for x in x_values]

pit.style.use('seaborn')
fig, ax = pit.subplots()
ax.scatter(x_values, y_values,  s=100)
# ax.plot(input_values, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# 目盛りラベルのサイズを設定する
ax.tick_params(axis='both', which='major', labelsize=14)

# 各軸の範囲を設定する
ax.axis([1, 5, 1, 125])

# グラフを自動保存にする
pit.savefig('square_plot.png', bbox_inches='tight')

# グラフを表示する
pit.show()

