# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        stack = []  # 用于记录从root根结点遍历到的结点
        res = []    # 用于记录中序遍历结点的值
        while root or stack:  # 循环终止条件为所有结点都已经遍历过，并且root指向None
            if root:  # 先将根结点入栈，如果有左孩子，则依次入栈，直至左子树为空，此时栈中记录的是所有根结点下的左结点
                stack.append(root)
                root = root.left
            else:     # 如果一个结点没有左右子树，则栈顶结点出栈，并且记录栈顶结点的值
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

if __name__ == '__main__':
    root = TreeNode(1)
    rroot = root
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root = root.left
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    s = Solution()
    print s.inorderTraversal(rroot)

####################################################################################
# 例如一棵二叉树为：  1
#                   /   \
#                  2     3
#                /   \     \
#               4     5     6
# 首先将根结点1入栈，有左孩子则依次入栈：1,2,4。由于4的左孩子为空则停止入栈，此时栈为
# {1，2，4}，此时将4出栈并遍历4，由于4也没有右孩子则继续出栈2，并遍历2,2有右孩子则将5
# 入栈，此时栈为{1，5}。
# 5没有左孩子则将5出栈并遍历5的右孩子。此时栈为{1}。
# 1有右孩子则将1出栈并遍历1的右孩子，重复上述步骤。