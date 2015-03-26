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
            for i in xrange(len(level)-1):  # 每一层的结点next指向该层下一个结点
                level[i].next = level[i+1]

    def levelOrder(self, root, level, res):  # 层次遍历，记录每一层的结点
        if root:
            if len(res) < level+1:
                res.append([])
            res[level].append(root)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)

    def connect(self, root):
        if root and root.left:  # 父结点的左子树next指向父结点的右子树结点
            root.left.next = root.right
            if root.next:  # 父结点的右子树next指向父子树next的左子树
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

###################################################################################
# 这道题用了两种解法：
# 方法一：对完全二叉树进行层次遍历，记录每一层的结点，然后每一层的结点next指向该层
# 下一个结点。
# 方法二：深度遍历，直接将二叉树父结点的左子树next指向父结点的右子树结点，然后父结点
# 的右子树next指向父子树next的左子树结点。
#