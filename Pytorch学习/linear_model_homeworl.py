import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# y = x*2.5-1 构造训练数据
x_data = [1.0, 2.0, 3.0]
y_data = [1.5, 4.0, 6.5]
W, B = np.arange(0.0, 4.1, 0.1), np.arange(-2.0, 2.1, 0.1) # 规定 W,B 的区间
w, b = np.meshgrid(W, B, indexing='ij') # 构建矩阵坐标

def forward(x):
    return x*w+b
    
def loss(y_pred, y):
    return (y_pred-y)*(y_pred-y)

# Make data.
mse_lst = []
l_sum = 0.
for x_val, y_val in zip(x_data, y_data):
    y_pred_val = forward(x_val)
    loss_val = loss(y_pred_val, y_val)
    l_sum += loss_val
mse_lst.append(l_sum/3)

# 定义figure
fig = plt.figure(figsize=(10,10), dpi=300)
# 将figure变为3d
ax = Axes3D(fig)
# 绘图，rstride:行之间的跨度  cstride:列之间的跨度
surf = ax.plot_surface(w, b, np.array(mse_lst[0]), rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# Customize the z axis.
ax.set_zlim(0, 40)
# 设置坐标轴标签
ax.set_xlabel("w")
ax.set_ylabel("b")
ax.set_zlabel("loss")
ax.text(0.2, 2, 43, "Cost Value", color='black')
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
