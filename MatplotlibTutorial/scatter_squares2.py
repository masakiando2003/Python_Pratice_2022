import matplotlib.pyplot as pit

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

pit.style.use('seaborn')
fig, ax = pit.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=pit.cm.Blues, s=10)
# ax.plot(input_values, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 目盛りラベルのサイズを設定する
ax.tick_params(axis='both', which='major', labelsize=14)

# 各軸の範囲を設定する
ax.axis([0, 1100, 0, 1100000])

pit.show()
