# coding=utf8

__author__ = 'smilezjw'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        res = []
        self.preorder(root, 0, res)
        res.reverse()  # reverse一下就可以了呢
        return res

    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)

##################################################################################
# 这道题在第102题的方法的基础上，直接对最后结果的列表reverse一下就可以了。
#