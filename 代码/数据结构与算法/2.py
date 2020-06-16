def Search(n):
    low = 0
    high = n
    # 前后两次的差值的绝对值 <= 0.0000000001, 则可退出
    while True:
        mid = (low + high) / 2
        if abs(mid * mid - n) < 0.0000000001:
            print(mid)
            return mid
        else:
            if mid * mid > n:
                high = mid
            if mid * mid < n:
                low = mid


if __name__ == "__main__":
    Search(5)
