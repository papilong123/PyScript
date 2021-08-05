# coding:utf-8
# !/usr/bin/python

table = {'abc': 1, 'def': 2, 'ghi': 3}
print(table)

# 字典反转
hashmap = dict([(v, k) for k, v in table.items()])
# 字典遍历
for key in hashmap.keys():
    print(key, ":", hashmap[key])

print(len(hashmap))
print(hashmap.keys())
print(hashmap.values())

# 字典的增，删，改，查
# 在这里需要来一句，对于字典的扩充，只需定义一个新的键值对即可，
# 而对于列表，就只能用append方法或分片赋值。
hashmap[4] = "xyz"
print(hashmap)

del hashmap[4]
print(hashmap)

hashmap[3] = "update"
print(hashmap)
