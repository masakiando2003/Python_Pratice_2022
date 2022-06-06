import matplotlib.pyplot as pit

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

pit.style.use('seaborn')
fig, ax = pit.subplots()
ax.scatter(x_values, y_values, s=100)
# ax.plot(input_values, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 目盛りラベルのサイズを設定する
ax.tick_params(axis='both', which='major', labelsize=14)

pit.show()
