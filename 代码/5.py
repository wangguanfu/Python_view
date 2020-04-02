"""
    生成器
        yield


"""


def coro():
    hello = yield "hello"  # 可以send值
    yield hello


# c = coro()
# # print(c)
# print(next(c))
# # print(c.send("world"))
# # print(c.send("world"))
#
# print(next(c))

# print(next(c))


"""
    单元测试
    unit Testing
        针对一个函数 一个累2
        
    三无代码
        无文档  无注释  无单测
    
    
    保证代码逻辑性
        高内聚低耦合
        
        
    回归测试
    
    
    
    单元测试库：
        nose/pytest
        
        
        mock 模块代替网络请求
        
        
        coverage  统计测试覆盖率
    
"""


def binary_search(array, target):
    if not array:
        return -1

    beg, end = 0, len(array)
    while beg < end:
        mid = beg + (end - beg) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid
        else:
            beg = mid + 1

    return -1


def test():
    assert binary_search([0, 1, 2, 3, 4, 5], 1) == 1
    assert binary_search([0, 1, 2, 3, 4, 5], 6) == -1
    assert binary_search([0, 1, 2, 3, 4, 5], 0) == -1
    assert binary_search([0, 1, 2, 3, 4, 5], 5) == 5



test()