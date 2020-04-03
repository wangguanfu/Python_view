"""
排序 和 查找  重中之重

排序: 冒泡  选择   归并

查找: 二分查找  线性

搜索:


链表操作: 翻转   插入   合并


"""


# 翻转 链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre


s = Solution()
l = ListNode(12345)
s.reverseList(l)
print(s.reverseList(l))





"""
用两个栈实现一个队列
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack1 == []:
            return None
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            out = self.stack2.pop()
            for j in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
            return out