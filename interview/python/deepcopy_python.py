#coding=utf-8

#使用copy.copy()，可以进行对象的浅拷贝，它复制了对象，但对于对象中的元素，依然使用原始的引用.

import copy

a = [1, 2, 3, 4, ['a', 'b'], {"abc": 123}]

b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(5)
a[4].append('c')
a[5]["abc"] = 321

print 'a = ', a
print 'b = ', b
print 'c = ', c
print 'd = ', d
