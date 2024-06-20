import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3,4,5])

G.add_edge(1,5)
G.add_edges_from([(1,2),(4,5),(3,2),(5,3)])

nx.draw(G,with_labels=True,node_color='purple',edge_color='black',node_size=2000,font_size=16)
plt.show()



# import numpy as np  
# import matplotlib.pyplot as plt  

# # 设置极坐标轴  
# fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))  
# # 定义玫瑰线的极坐标方程  
# theta = np.linspace(0, 2. * np.pi, 1000)  
# r = np.sin(2 * theta) * np.sin(theta / 10.)  # 这里只是一个简单的玫瑰线方程  
# # 绘制玫瑰线  
# ax.plot(theta, r, color='purple')  
# # 隐藏极坐标的网格线  
# ax.grid(False)  
# # 设置标题  
# ax.set_title("Rose Curve", va='bottom')  
# # 显示图形  
# plt.show()


# import numpy as np  
# import matplotlib.pyplot as plt  
  
# # 设置角度范围  
# theta = np.linspace(0, 2 * np.pi, 1000)  
  
# # 玫瑰曲线的极坐标方程，这里使用了一个简单的玫瑰曲线方程  
# # 你可以尝试修改这个方程来得到不同的玫瑰形状  
# r = np.sin(2 * theta) * np.sin(theta / 3.) * 5  # 调整5来控制花朵大小  
  
# # 转换为笛卡尔坐标  
# x = r * np.cos(theta)  
# y = r * np.sin(theta)  
  
# # 绘制曲线  
# fig, ax = plt.subplots()  
# ax.plot(x, y, color='purple')  
  
# # 设置标题和坐标轴标签（虽然极坐标中不需要，但在这里保留以作说明）  
# ax.set_title('Rose Curve')  
# ax.set_xlabel('X Axis')  
# ax.set_ylabel('Y Axis')  
  
# # 设置坐标轴比例相等以保持玫瑰的形状  
# ax.set_aspect('equal', 'box')  
  
# # 显示图形  
# plt.show()