# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preOrder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:  # 如果是双数行，则从左到右记录结点的数值
                res[level].append(root.val)
            else:               # 如果是单数行，则从右到左反过来记录结点的数值
                res[level].insert(0, root.val)
            self.preOrder(root.left, level+1, res)
            self.preOrder(root.right, level+1, res)

    def zigzagLevelOrder(self, root):
        res = []
        self.preOrder(root, 0, res)
        return res

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    p = root
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root = root.right
    root.left = TreeNode(15)
    root.right = TreeNode(7)
    print s.zigzagLevelOrder(p)

##################################################################################
# 这道题和第102题思路类似，只是区分单数行从左到右记录结点值，双数行从右到左记录结
# 点值。
#