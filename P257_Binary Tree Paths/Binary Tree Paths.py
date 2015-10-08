# coding=utf8

__author__ = 'smilezjw'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        self.dfs(root, '', res)
        return res


    def dfs(self, root, path, res):
        if root and root.left is None and root.right is None:
            res.append(path + str(root.val))
            return
        elif root:
            path += str(root.val) + '->'
            self.dfs(root.left, path, res)
            self.dfs(root.right, path, res)

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    curr = root
    curr.left = TreeNode(2)
    curr.right = TreeNode(3)
    curr = curr.left
    curr.right = TreeNode(5)
    print s.binaryTreePaths(root)