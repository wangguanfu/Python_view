"""
        python 函数传参常考问题

    常考点：
    -参数传递
    -(不)可变参数
    -可变参数


"""


####  考察的知识点 --- 传参方式  ---可变对象
# 可变参数
def flist(l):
    l.append(0)
    print(l)


l = []
flist(l)
flist(l)


# 不可变参数
def fstr(s):
    s += 'a'
    print(s)


s = 'hehe'
fstr(s)
fstr(s)
"""
对象引用传参  --  共享传参

什么是变量(一切皆对象)  
    

"""


# 默认参数只计算一次
def fl(l=[1]):
    l.append(1)
    print(l)


fl()
fl()


"""
python *args **kwargs
    
"""



