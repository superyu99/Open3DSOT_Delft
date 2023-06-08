import torch

# 创建大小为 [2, 1024, 5] 的张量
tensor1 = torch.randn((2, 1024, 5))

# 创建大小为 [2, 1024, 3] 的张量
tensor2 = torch.randn((2, 512, 3))

# 在第三个维度上拼接张量
concatenated_tensor = torch.cat([tensor1[:, :512, :], tensor2], dim=2)

# 将拼接后的部分替换原始张量的前一半部分
tensor1[:, :512, :] = concatenated_tensor[:, :512, :]

# 打印替换后的张量的形状
print(tensor1.shape)