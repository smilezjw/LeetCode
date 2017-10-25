# coding=utf8

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # This solution is common for all kinds of binary tree
        # trimRoot = None
        # if root is None:
        #     return root
        # elif L <= root.val <= R:
        #     trimRoot = TreeNode(root.val)
        #     trimRoot.left = self.trimBST(root.left, L, R)
        #     trimRoot.right = self.trimBST(root.right, L, R)
        # else:
        #     trimRoot = self.trimBST(root.left, L, R) or self.trimBST(root.right, L, R)
        # return trimRoot

        # This solution is only for binary search tree
        if root is None:
            return root
        elif root.val > R:
            root = self.trimBST(root.left, L, R)
        elif root.val < L:
            root = self.trimBST(root.right, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        return root

    def DFS(self, root):
        if root is None:
            return root
        print root.val
        self.DFS(root.left)
        self.DFS(root.right)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    p = root.left
    p.left = TreeNode(4)
    p.right = TreeNode(2)

    solution = Solution()
    print solution.DFS(root)
    print '---'
    trimRoot = solution.trimBST(root, 1, 2)
    print solution.DFS(trimRoot)
