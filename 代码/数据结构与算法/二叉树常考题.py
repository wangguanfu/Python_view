"""
    层序遍历二叉树：
        广度优先:
            判断根 存在 和下一个节点存在  就添加进去
              -层层 放



        深度优先 ： 用level 来查找出每一个值 然后填充进去

                切面放进去
"""

#  广度优先

import collections


class Solution:
    def levelOrder(self, root):
        if not root: return []

        res = []
        queue = collections.deque()
        queue.appendleft(root)

        while queue:
            level_size = len(queue)
            cur = []

            for _ in range(level_size):
                node = queue.popleft()
                cur.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(cur)

        return res


class solution:
    def levelOrder(self, root):

        res = []
        cur_nodes = [root]
        next_nodes = []

        res.append([i.val for i in cur_nodes])

        while cur_nodes or next_nodes:
            for node in cur_nodes:
                if node.left: next_nodes.append(node.left)
                if node.right: next_nodes.append(node.right)

            if next_nodes:
                res.append(
                    [i.val for i in next_nodes]
                )
            cur_nodes = next_nodes
            next_nodes = []

        return res


# 深度优先  递归的写法

class Sulut:
    def levelOrder(self, root):
        if not root: return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node: return []

        if len(self.result) < level + 1:
            self.result.append([])

        self.result[level].append(node.val)

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
