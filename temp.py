import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=3, suppress=True)

# 读取txt文件中的数据
data = np.loadtxt('/workspace/sot/Open3DSOT/watch_if_speed_is_acurate_Car.txt', delimiter=',')
index = np.abs(data[:,5]) <= 10
data = data[index]

# 计算每列的均值、最小值和最大值
mean_values = np.mean(data, axis=0)
var = np.var(data, axis=0)
min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)

print("Mean values:", mean_values)
print("Var",var)
print("Min values:", min_values)
print("Max values:", max_values)

# # 绘制直方图并将其保存到磁盘
# column_names = ['x_mean', 'x_min', 'x_max', 'y_mean', 'y_min', 'y_max']

# for i, column_name in enumerate(column_names):
#     plt.hist(data[:, i], bins=20)
#     plt.xlabel(column_name)
#     plt.ylabel('Frequency')
#     plt.title(f'Histogram of {column_name}')
#     plt.savefig(f'{column_name}_histogram.png')  # 保存直方图到磁盘
#     plt.clf()  # 清除当前图形，以便绘制下一个直方图