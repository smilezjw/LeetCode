# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        # 递归求解每个结点的左右子树高度差，如果大于1则直接return False，否则可以递归求解
        if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def Height(self, root):  # 求解二叉树的高度
        if root is None:
            return 0
        # 二叉树的高度定义为max(左子树高度,右子树高度）+ 1, 因为要算上根结点
        return max(self.Height(root.left), self.Height(root.right)) + 1

if __name__ == '__main__':
    root = TreeNode(1)
    p = root
    root.right = TreeNode(2)
    root = root.right
    root.right = TreeNode(3)
    s = Solution()
    print s.isBalanced(p)

#######################################################################################
# 这道题求解思路：首先实现函数用于计算二叉树的高度，然后递归求解每个结点左右子树的高度
# 差，如果高度差大于1则直接return False，否则继续递归求解。
#