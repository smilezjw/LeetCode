# coding=utf8

__author__ = 'smielzjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        # 判断两个结点是否相互独立，并且值是否相等
        elif (p is None or q is None) or not (p != q and p.val == q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

####################################################################################
# 这道题比较简单，首先判断两个根结点是否相同，如果相同则递归判断左右子树是否相同。
# 判断两棵树是否相同，需要判断结点是否独立，并且结点的值是否相等。
#