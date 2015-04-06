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
        leftMax = rightMax = 0
        if root.left:
            leftMax = self.dfs(root.left)  # 深度递归，得到左子树的最大值
            if leftMax > 0:
                sum += leftMax
        if root.right:
            rightMax = self.dfs(root.right)  # 深度递归，得到右子树的最大值
            if rightMax > 0:
                sum += rightMax
        if sum > Solution.max:
            Solution.max = sum  # 全局变量记录路径的最大和
        return max(root.val, max(root.val + leftMax, root.val + rightMax))


if __name__ == '__main__':
    root = TreeNode(2)
    p = root
    root.left = TreeNode(-1)
    root.right = TreeNode(3)
    s = Solution()
    print s.maxPathSum(p)

#######################################################################################
# 这道题的意思是在树中找到一条路径使得该路径上的节点和最大，起点和终点只要是树中的节点
# 即可。但是节点值可能为负。
# 深度递归，用全局变量记录每个子树的最大路径和。
#