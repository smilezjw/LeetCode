# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        Solution.res = []
        if root is None:
            return Solution.res
        self.dfs(root, sum, [])
        return Solution.res

    def dfs(self, root, sum, value):
        if root is None:
            return
        if root.left is None and root.right is None and root.val == sum:
            Solution.res.append(value + [root.val])
        else:
            self.dfs(root.left, sum - root.val, value + [root.val])
            self.dfs(root.right, sum - root.val, value + [root.val])

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    p = root
    root.left = TreeNode(-2)
    root.right = TreeNode(3)
    print s.pathSum(p, -1)

######################################################################################
# 这道题和上道题P112是类似的，就是这道题需要用全局变量来记录遍历的结点。
#