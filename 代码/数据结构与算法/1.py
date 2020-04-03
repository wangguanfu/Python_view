# collections
"""
内置：
    list/tuple   array
    collections.deque(双端队列  栈)

    dict      collections.Counter OrdererdDict


    sorted


    bisect模块
    heapq


"""

# namedtuple
import collections

Point = collections.namedtuple('point', 'x, y')

p = Point(1, 2)
print(p.x, p.y)

print(p[0], p[1])

# deque

de = collections.deque()

de.append(1)
de.appendleft(0)

print(de)
print(de.pop())
print(de.popleft())

# Counter

d = collections.Counter("qweqrqdasdq")
print(d)

print(d["a"])
print(d.most_common())

# orderedDict

od = collections.OrderedDict()

od["c"] = 'c'
od['b'] = 'b'
od['a'] = 'a'

print(od.keys())

for i in od.keys():
    print(i)

# defaultDict 默认值


"""

dict 哈希表 
时间复杂度 可以  o(1）
二次探查解决哈希冲突的   (线性  二次)  链表法

"""

"""
LRUCache
    最近最少使用
    
    
    
"""


# dict  Orderdict

class LRUCache:

    def __init__(self, cap=128):
        self.od = collections.OrderedDict()
        self.cap = cap

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.od:
            del self.od
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.cap:
                self.od.popitem(last=False)
