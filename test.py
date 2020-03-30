"""
    最近邻元法、双线性插值
"""
from math import sqrt as sqrt


# 求距离
def dis(x1, y1, x2, y2):
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


# 最近邻元法
def near_func(x, y):
    dis_1 = dis(1, 1, x, y)
    dis_2 = dis(1, 2, x, y)
    dis_3 = dis(2, 1, x, y)
    dis_4 = dis(2, 2, x, y)
    min_dis = min(dis_1, dis_2, dis_3, dis_4)
    if min_dis == dis_1:
        return 5
    elif min_dis == dis_2:
        return 1
    elif min_dis == dis_3:
        return 4
    elif min_dis == dis_4:
        return 3


# print(near_func(1.2, 1.6))


# 双线性插值
def double_func(x, y, flag='x'):
    if flag == 'x':
        # 首先对x方向进行插值
        a = (2 - x) * 5 + (x - 1) * 4
        b = (2 - x) * 1 + (x - 1) * 3
        # 对y方向进行插值
        return (2 - y) * a + (y - 1) * b
    elif flag == 'y':
        # 首先对y方向进行插值
        aa = (2 - y) * 5 + (y - 1) * 1
        bb = (2 - y) * 4 + (y - 1) * 3
        # 对x方向进行插值
        return (2 - x) * aa + (x - 1) * bb


print(double_func(1.2, 1.6, 'x'))
print(double_func(1.2, 1.6, 'y'))
