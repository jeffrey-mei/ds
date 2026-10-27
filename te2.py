#默认参数是同一个列表
def add_item_bad(x,bucket=[]):
    bucket.append(x)
    return bucket
print(add_item_bad(1))
print(add_item_bad(2))
print(add_item_bad(3))

def add_item_ok(x,bucket=None):
    if bucket == None:
        bucket =[]
    bucket.append(x)
    return bucket
print(add_item_ok(1))
print(add_item_ok(2))
print(add_item_ok(3))

#引用传递 ： 数组的传参 本质只传了地址
def fill_zero(rows):
    for row in rows:
        row[0] = 0
    return rows
data = [[1,2],[3,4]]
print(fill_zero(data))
print(data)