# 定义元组
demensions = (200,50)
print(demensions[0])
print(demensions[1])

# 错误：不能修改元组的元素值
# demensions[0] = 250

# 修改元组变量，虽然不能修改元组的元素，但可以给存储元组的变量赋值
demensions = (400,100)
for demension in demensions:
    print(demension)