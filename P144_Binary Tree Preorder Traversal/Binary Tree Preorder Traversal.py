# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 深度优先搜索,耗时46ms
    def preorderTraversal(self, root):
        Solution.res = []
        self.preOder(root)
        return Solution.res

    def preOder(self, root):
        if root:
            Solution.res.append(root.val)
            self.preOder(root.left)
            self.preOder(root.right)

    # 用栈操作非递归，耗时43ms
    def preorderTraversal_Stack(self, root):
        stack = []
        res = []
        while root or stack:
            # 首先遍历根节点的左子树直至叶子结点
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            # 开始出栈，判断当前结点是否有右子树
            else:
                root = stack.pop()
                root = root.right
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    p = root.left
    p.left = TreeNode(4)
    p.right = TreeNode(5)
    print s.preorderTraversal(root)
    print s.preorderTraversal_Stack(root)

###########################################################################################
# 先序遍历二叉树用递归实现比较简单。题目要求用非递归方法，考虑用栈来实现。
# 首先遍历根节点并入栈，继续遍历其左子树并入栈；
# 直至当前结点没有左孩子为止开始出栈，每次出栈判断是否有右子树，如果有右子树继续入栈重复上
# 述操作，否则继续出栈。直至节点为None并且栈为空。
# 画个图比较清楚。