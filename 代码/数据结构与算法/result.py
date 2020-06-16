class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head):
    """链表逆序"""
    if head == None or head.next == None:
        return
    cur = head.next
    next = cur.next
    pre = cur
    cur.next = None
    cur = next
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    cur.next = pre
    head.next = cur


if __name__ == '__main__':
    s = Node([1, 2, 3])
    print(reverse(s))




# def Search():
#     low = 2.2
#     high = 2.3
#     mid = (low + high) / 2
#     # 前后两次的差值的绝对值 <= 0.0000000001, 则可退出
#     while abs(high - low) > 0.0000000001:
#         if high * high > 5:
#             high = mid
#         else:
#             low = mid
#         mid = (low + high) / 2
#     print("最终的low 的值: % s" % low)
#     print("最终的high的值: % s" % high)
#     print("最终的mid 的值: % s" % mid)
#     return mid
#
# if __name__ == "__main__":
#     Search()


