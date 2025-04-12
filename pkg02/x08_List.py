#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-13:32

lst = ["Hello", 123, 3.14]
print(lst, type(lst), id(lst))

print(lst[0], type(lst[0]), id(lst[0]))
print(lst[1], type(lst[1]), id(lst[1]))
print(lst[2], type(lst[2]), id(lst[2]))

# 列表变量存储的是列表的地址，而列表内存储是变量的引用

print('-------------列表创建方式------------------')
ls1 = [1, 2, 3.14]
ls2 = list([10, 11, 12])
print(ls1)
print(ls2)

print('-------------列表 index() 操作-----------------')
lst = ["Hello", 123, 3.14, 'Hello']
print(lst.index('Hello'))  # 只返回第一个出现的位置
# print(lst.index('Ok')) 不存在的元素，报错 ValueError
print(lst.index('Hello', 1, 4))  # 可指定区间查找

print('-------------列表下标操作-----------------')
lst = ["Hello", 123, 3.14, 'Hello']
print(lst[0])
print(lst[0:4])
print(lst[-4])
print(lst[-4:])
print(lst[-4::2])  # [start:stop:step]

print('-------------列表拷贝-----------------')
lst2 = lst[0:]
print("lst", id(lst))
print("lst2", id(lst2))
print("lst[0]", id(lst[0]))
print("lst2[0]", id(lst2[0]))

print('-------------列表步长为负数-----------------')
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[::-1])
print(lst[3::-1])

print('-------------列表迭代输出-----------------')
lst = [1, 2, 3, 4, 5, 6, 7, 8]
for value in lst:
    print(value)

print('-------------列表添加元素-----------------')
lst = [1, 2, 3, 4, 5, 6]
print("原列表：", lst)
lst.append(11)
print("append：", lst)

lst2 = ["Hello", "World"]
lst.extend(lst2)
print("extend：", lst)

lst.insert(0, "OK")
print("insert：", lst)

lst[2:] = lst2
print("切片：", lst)

print('-------------列表删除元素-----------------')
lst = [10, 20, 30, 40, 50, 60, 20]
print("原列表：", lst)

lst.remove(20)
print("remove：", lst)  # remove 只删除第一个出现的元素，重复的后续不删

lst.pop()
print("pop：", lst)  # 删除列表最后一个元素，可以指定索引

lst[2:] = []
print("切片操作", lst)

lst.clear()
print(lst)

del lst

print('-------------列表修改元素-----------------')
lst = [10, 20, 30, 40, 50, 60, 20]
print("原列表：", lst)

lst[1] = 200
print(lst)

lst[1:] = [1]
print(lst)

print('-------------列表排序-----------------')
lst = [3, 2, 5, 8, 4, 7, 6, 9]
print("原列表：", lst)

# lst.sort()
# print(lst)
#
# lst.sort(reverse=True)
# print(lst)

new_lst = sorted(lst)
print(new_lst)
desc_lst = sorted(lst, reverse=True)
print(desc_lst)


print('-------------列表生成式-----------------')

lst = [i**3 for i in range(1,9)]
print(lst)