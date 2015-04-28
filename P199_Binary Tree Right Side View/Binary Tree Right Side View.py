# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 深度优先搜索
    def rightSideView(self, root):
        Solution.res = []
        self.dfs(root, 1)
        return Solution.res

    # 层次遍历，level记录遍历节点所在的层次，这里默认根结点所在的层次为0
    def dfs(self, root, level):
        if root:
            # 如果该结点所在的层次小于列表长度，说明该层的最右边节点已经找到了
            if level > len(Solution.res):
                Solution.res.append(root.val)
            # 先找最右边的节点，再遍历左边的节点
            self.dfs(root.right, level+1)
            self.dfs(root.left, level+1)

    # 用队列实现宽度优先搜索
    def rightSideView_Queue(self, root):
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            length = len(queue)
            for i in xrange(length):
                node = queue.pop(0)
                # 因为最先进入队列的是最右边的节点，因此只将第一个出队列的节点保存到结果列表中
                if i == 0:
                    res.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    p = root.left
    p.right = TreeNode(5)
    p = root.right
    p.right = TreeNode(4)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    p = root2.left
    p.left = TreeNode(4)
    print s.rightSideView(root)
    print s.rightSideView_Queue(root2)

#####################################################################################
# 这道题采用层次遍历的思路求解，可以用递归深度优先遍历，也可以用队列实现宽度优先遍历。
# 注意先遍历右边节点，再遍历左边节点，只需要返回每一层最右边的节点即可。
#