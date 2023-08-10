import numpy as np
from scipy import stats

# 输入一组数字，以空格分隔
data = input("请输入一组数字，以空格分隔：")
data = list(map(float, data.split()))

# 计算统计学的基础数据
mean = np.mean(data)  # 平均值
median = np.median(data)  # 中位数
std_dev = np.std(data)  # 标准差
min_value = np.min(data)  # 最小值
max_value = np.max(data)  # 最大值
variance = np.var(data)  # 方差
mode = stats.mode(data)  # 众数

# 打印结果
print("平均值：", mean)
print("中位数：", median)
print("标准差：", std_dev)
print("最小值：", min_value)
print("最大值：", max_value)
print("方差：", variance)
print("众数：", mode.mode)

