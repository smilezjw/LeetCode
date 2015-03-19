# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        Solution.maxDep = 0
        self.preOrderTraversal(root, 0)
        return Solution.maxDep

    def preOrderTraversal(self, root, level):
        Solution.maxDep = max(level, Solution.maxDep)  # 记录当前最大深度
        if root:
            self.preOrderTraversal(root.left, level+1)  # 先序遍历
            self.preOrderTraversal(root.right, level+1)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    curr = root
    curr.left = TreeNode(1)
    curr.right = TreeNode(2)
    curr = curr.right
    curr.left = TreeNode(5)
    curr.right = TreeNode(6)
    print s.maxDepth(root)

########################################################################################
# 这道题使用深度优先搜索，先序遍历二叉树，用level变量记录当前遍历的二叉树的层数，用全局
# 变量maxDep比较最大二叉树的深度。到了叶子结点往下遍历level还会加1，弥补了根结点从0开始
# 计算的问题。
#
