import torch.nn as nn

# 注意torch.nn.Module.modules()和torch.nn.Module.children()方法的区别:
#
# 前者modules()会递归地遍历所有子模块,
# 包括子模块的子模块、子模块的子模块的子模块,等等依此类推.
#
# 后者children()只会遍历所有直接子模块,不再递归下去,
# 即子模块的子模块不会被遍历到.

# modules()  modules()方法
#     Returns an iterator over all modules in the network.
#     返回一个迭代器,这个迭代器能够遍历神经网络中的所有模块.
#     Yields  迭代返回
#         Module – a module in the network
#         Module类型 - 神经网络中的一个模块
#
#     Note  注意:
#     	Duplicate modules are returned only once.
#     	重复的模块只返回一次.
#     	In the following example, l will be returned only once.
#     	在以下例子中,模块对象lin只返回一次.

lin = nn.Linear(2, 2)
net = nn.Sequential(lin, lin)
for idx, m in enumerate(net.modules()):
    print(idx, '->', m)
