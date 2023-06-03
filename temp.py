import torch
from pointnet2.utils.pointnet2_utils import QueryAndGroup

# 创建只包含一个点的点云1和点云2
point_cloud1 = torch.tensor([[[0.1, 0.0, 0.0],
															[0.11,0.0, 0.0]]], device='cuda').float() #1*1*3
point_cloud2 = torch.tensor([[[0.4, 0.0, 0.0]]], device='cuda').float() #1*1*3

# 初始化QueryAndGroup模块
search_radius = 0.2
max_neighbors = 1
QA = QueryAndGroup(search_radius, max_neighbors)

# 将点云2作为中心，点云1作为查询点
output = QA(point_cloud2, point_cloud1) #1*3*1*1


# 调整输出张量的形状
output_reshaped = output.squeeze(3).transpose(1, 2)

# 检查是否有距离大于搜索半径的邻域点
distances = output_reshaped.norm(p=2, dim=-1)  # 计算距离
mask = distances <= search_radius  # 创建一个距离小于等于搜索半径的布尔掩码
output_reshaped = output_reshaped * mask.unsqueeze(-1).float()  # 将距离大于搜索半径的邻域点坐标设置为零
print(output_reshaped)

# 将输出结果添加到point_cloud1，以便获取邻域点的坐标
neighbor_point_coordinates = point_cloud1 + output_reshaped
print(neighbor_point_coordinates)
print(neighbor_point_coordinates.shape)