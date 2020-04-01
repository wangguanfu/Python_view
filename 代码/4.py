"""
Python  性能的分析和优化   GIL常考问题  Cpython 并不是线程安全的
        使用锁机制  避免
        CPU密集 影响很大
        IO期间 会释放 GIL  对io密集 影响小




"""

import threading

n = [0]


def foo():
    n[0] = n[0] + 1
    n[0] = n[0] + 1
    print(n)

foo()


# threads = []
# for i in range(5000):
#     t = threading.Thread(target=foo)
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# print(n)


"""
    profile  工具      pyflame 开源工具
    
    web 应用 语言一般不会是瓶颈
    
    
    数据结构与算法
    
    数据库层: 索引  nosql
     
    网络
    
    缓存  
    
    异步  asyncio celery
    
    并发  gevent/多线程
    
"""








