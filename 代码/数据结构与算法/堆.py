""""
堆 : 完全二叉树
合并多个有序数组和链表  TopK 问题

python 内置模块 heapq



"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        if res == []:
            return []
        res.sort()
        l = ListNode(0)
        first = l
        while res:
            l.next = ListNode(res.pop(0))
            l = l.next
        return first.next


































