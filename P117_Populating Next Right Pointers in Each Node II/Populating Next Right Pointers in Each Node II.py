# coding=utf8

__author__ = 'smilezjw'


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        res = []
        self.levelOrder(root, 0, res)
        for level in res:
            for i in xrange(len(level)-1):
                level[i].next = level[i+1]

    def levelOrder(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.append([])
            res[level].append(root)
            self.levelOrder(root.left, level+1, res)
            self.levelOrder(root.right, level+1, res)

###############################################################################
# 这道题我还是采取了层次遍历，然后每一层的结点依次指向下一个结点。
#