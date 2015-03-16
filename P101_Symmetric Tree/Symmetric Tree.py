# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            return self.symmetric(root.left, root.right) and self.symmetric(root.right, root.left)

    def symmetric(self, leftChild, rightChild):
        if leftChild == rightChild == None:  # 如果左右子树都为空，则返回True
            return True
        elif leftChild and rightChild and leftChild.val == rightChild.val:
            return self.symmetric(leftChild.left, rightChild.right) and self.symmetric(leftChild.right, rightChild.left)
        return False

#######################################################################################
# 首先判断根结点是否为空，如果不为空则判断根结点的左右子树的根结点是否相等，然后递归
# 判断左子树的左孩子结点和右子树的右孩子结点，以及左子树的右孩子结点和右子树的左孩子
# 结点是否相等。
#