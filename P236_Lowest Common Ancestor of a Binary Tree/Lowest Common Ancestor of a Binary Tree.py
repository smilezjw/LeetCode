# coding=utf8

__author__ = 'smilezjw'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # 找到目标结点，则通过返回值标记该子树发现了某个目标结点
        if root is None or root == p or root == q:
            return root
        # 查看左子树中是否有目标结点，没有为None
        left = self.lowestCommonAncestor(root.left, p, q)
        # 查看右子树中是否有目标结点，没有为None
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左右子树分别找到目标结点，说明该祖先结点为最近公共祖先结点
        if left is not None and right is not None:
            return root
        # 否则，一个结点是另一个结点的祖先结点，返回不为空的结点即为最近公共祖先结点
        return right if left is None else left


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    p = root
    p.left = TreeNode(5)
    p = p.left
    m = p
    p.left = TreeNode(6)
    p.right = TreeNode(2)
    n = p.right
    p = root
    p.right = TreeNode(1)
    p = p.right
    p.left = TreeNode(0)
    p.right = TreeNode(8)
    res = s.lowestCommonAncestor(root, m, n)
    print res.val if res else res

