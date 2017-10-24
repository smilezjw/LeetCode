# coding=utf8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        p = TreeNode(t1.val + t2.val)
        p.left = self.mergeTrees(t1.left, t2.left)
        p.right = self.mergeTrees(t1.right, t2.right)
        return p

if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)

    solution = Solution()
    tree = solution.mergeTrees(t1, t2)
    print tree.left.left.val