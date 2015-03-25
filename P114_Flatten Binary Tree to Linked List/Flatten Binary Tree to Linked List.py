# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten_list(self, root):
        Solution.value = []
        self.preOrder(root)
        curr = root
        for val in Solution.value[1:]:
            curr.left = None
            curr.right = TreeNode(val)
            curr = curr.right
        curr.left = None
        curr.right = None

    def preOrder(self, root):
        if root:
            Solution.value.append(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def flatten(self, root):
        if root is None:
            return
        # 先序遍历左子树的最后一个非叶子结点
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left is None:
            return
        p = root.left
        while p.right:
            p = p.right
        # 将该非叶子结点右边的结点链接到左子树上去
        p.right = root.right
        # 然后将该非叶子结点的左子树作为该非叶子结点的右子树
        root.right = root.left
        # 将该非叶子结点的左子树设为None
        root.left = None
        return root

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    p = root
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root = root.left
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    print s.flatten(p)

####################################################################################
# 一开始的思路是对二叉树进行先序遍历，将结点的值记录到列表中，然后重新对根结点构建
# 二叉树。但是这样做貌似不是题目希望的解法。
# 然后改写，首先先序遍历找到左子树最后一个非叶子结点，然后将该结点的右孩子结点链接到
# 左孩子结点上，然后将修改后的左子树变成其右子树，并将其左子树改为None。依次先序遍历
# 重复操作。
#