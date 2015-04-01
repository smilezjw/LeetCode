# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        if root is None:
            return 0
        Solution.res = []
        self.dfs(root, str(root.val))
        res = 0
        for num in Solution.res:  # 将所有从根结点到叶子结点的值进行相加
            res += num
        return res

    def dfs(self, root, value):  # 深度搜索，记录从root到leaf各个结点的值
        if root.left:
            self.dfs(root.left, value+str(root.left.val))
        if root.right:
            self.dfs(root.right, value+str(root.right.val))
        # 到达叶子结点则记录从根结点到该叶子结点的路径上的值
        if root.left is None and root.right is None:
            Solution.res.append(int(value))

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    s = Solution()
    print s.sumNumbers(root)

########################################################################################
# 今天终于做出来一道题了。
# 这道题使用深度优先搜索，判断停止条件比较重要，一开始在停止条件上出了点错误。
#