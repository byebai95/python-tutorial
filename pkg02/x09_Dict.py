#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-14:24

print('-------------字典的创建-------------')
# 第一种 空字段
dic1 = {}
print(dic1, type(dic1))

# 第二种
dic2 = {'name': 'jack', 'age': 20}
print(dic2, type(dic2))

# 第三种
dic3 = dict(name='Lucy', age=22)
print(dic3, type(dic3))

print('-------------字典查找-------------')
dic = {'name': 'jack', 'age': 20}
print("原字典:", dic)

print(dic['name'])
# print(dic['address']) ,报错，KeyError

print(dic.get('name'))
print(dic.get('address'))

# 当 key 不存在，返回默认值
print(dic.get('address', '北京'))

print('-------------字典增删改-------------')
dic = {'jack': 22, 'lucy': 20}
print("原字典:", dic)

dic['bob'] = 25  # 字典新增

dic['jack'] = 100  # 字典修改
print(dic)

dic.clear()

del dic

print('-------------字典视图-------------')
dic = {'jack': 22, 'lucy': 20}
print("原字典:", dic)

keys = dic.keys()
print(keys, type(keys))

values = dic.values()
print(values, type(values))

items = dic.items()
print(items)

print('-------------字典遍历-------------')
dic = {'jack': 22, 'lucy': 20}
print("原字典:", dic)

for key in dic:
    print(key, dic[key], dic.get(key))

# 字典的 key 必须是比可变的对象，当前有 string 与 整数

print('-------------字典生成式-------------')

lst1 = ['apple', 'orange', 'banana']
lst2 = [10.1, 3.14, 2.3, 3.2]
dic = {name: price for name, price in zip(lst1, lst2)} # zip() 内置函数可以将2个列表打包成元组列表进行返回
print(dic)
