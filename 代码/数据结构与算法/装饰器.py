import time


def func_time(func):
    def inner(*args, **kwargs):
        now_time = time.localtime()
        print('函数开始运行的时间为：', time.strftime('%Y:%m:%d %H:%M:%S', now_time))
        return func(*args, **kwargs)

    return inner


@func_time
def sum(x, y):
    print(x, y)


sum(4, 7)
