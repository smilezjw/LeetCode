# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 首先对二叉查找树进行中序遍历，记录中序遍历得到的结点和结点的值
    def recursiveInorderTraversal(self, root, listp, listValue):
        if root:
            self.recursiveInorderTraversal(root.left, listp, listValue)
            listp.append(root)
            listValue.append(root.val)
            self.recursiveInorderTraversal(root.right, listp, listValue)

    def recoverTree(self, root):
        listp = []
        listValue = []
        self.recursiveInorderTraversal(root, listp, listValue)
        # 对结点值进行排序，因为二叉查找树中序遍历的结点值必定是递增的
        listValue.sort()
        # 然后对每个结点赋予对应的结点的值
        for i in xrange(len(listp)):
            listp[i].val = listValue[i]
        return root

####################################################################################
# 这里采用的解法思路是二叉查找树的中序遍历是升序的，因此需要对二叉查找树进行中序
# 遍历，用两个列表记录中序遍历的结点和结点值，然后对记录结点值的列表进行排序，最后
# 将结点值依次赋予结点即可。
#