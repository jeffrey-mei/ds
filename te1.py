import copy

a = [[1,2],[3,4]]
b = a[:]  # 浅拷贝  
b[0][0] = 99
print(a)

c = copy.deepcopy(a)
c[0][0] = 0
print(a)

d = [1,2,3,4,5,6,7,9]
print(d[1:4])
print(d[:4])
print(d[-2:])
print(d[::2])
print(d[::-1])
print(d[4:100])

# 给定两个浮点数 判断它的和是否为0.3

