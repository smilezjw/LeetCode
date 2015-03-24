# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    p = root
    root.left = TreeNode(-2)
    root.right = TreeNode(3)
    print s.hasPathSum(p, -1)