# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        Solution.max = -2**31
        if root is None:
            return 0
        self.dfs(root)
        return Solution.max

    def dfs(self, root):
        if root is None:
            return 0
        sum = root.val
        leftMax = 0
        rightMax = 0
        if root.left:
            leftMax = self.dfs(root.left)
            if leftMax > 0:
                sum += leftMax
        if root.right:
            rightMax = self.dfs(root.right)
            if rightMax > 0:
                sum += rightMax
        if sum > Solution.max:
            Solution.max = sum
        return max(root.val, max(root.val+leftMax, root.val+rightMax))


if __name__ == '__main__':
    root = TreeNode(2)
    p = root
    root.left = TreeNode(-1)
    root.right = TreeNode(3)
    s = Solution()
    print s.maxPathSum(p)