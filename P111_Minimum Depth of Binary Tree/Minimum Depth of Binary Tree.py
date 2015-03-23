# coding=utf8

__author__ = 'dell'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        Solution.minDep = 2 ** 31 - 1
        self.preOrder(root, 1)
        return Solution.minDep

    def preOrder(self, root, level):
        if root and root.left is None and root.right is None:
        # 判断是否为叶子结点，计算叶子结点所处的高度
            Solution.minDep = min(level, Solution.minDep)
        elif root:
            # 先序遍历
            self.preOrder(root.left, level+1)
            self.preOrder(root.right, level+1)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    p = root
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root = root.right
    root.left = TreeNode(5)
    root = root.left
    root.left = TreeNode(6)
    print s.minDepth(p)

#######################################################################################
# 先序遍历二叉树，判断是否为叶子结点，计算叶子结点所处的树的高度，得到二叉树的最小高度。
#