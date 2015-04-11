# coding=utf8

__author__ = 'dell'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归遍历
    def postorderTraversal(self, root):
        Solution.res = []
        self.postOrder(root)
        return Solution.res

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            Solution.res.append(root.val)

    # 使用栈非递归遍历
    def postorderTraversal_Stack(self, root):
        res = []
        stack = [root]
        while root and stack:
            # 首先深度优先搜索找到左子树的最后一个结点
            if root and root.left:
                root = root.left
                stack.append(root)
            # 然后判断是否有右孩子
            elif root and root.right:
                root = root.right
                stack.append(root)
            # 如果当前结点没有左右孩子，才能添加到结果列表中
            else:
                curr = stack.pop()
                res.append(curr.val)
                # 为了避免死循环，这里修改父结点的左右指针
                if len(stack) > 0:
                    root = stack[-1]
                    if root.left == curr:
                        root.left = None
                    elif root.right == curr:
                        root.right = None
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print s.postorderTraversal_Stack(root)

##########################################################################################
#                    1
#                  /   \
#                 2     3
#               /   \
#              4     5
# 1.首先将根结点入栈，然后遍历根结点的左子树，如果有左孩子则入栈；直到左子树最后一个左孩子
# 结点，此时栈为stack == [1, 2, 4]， 指针指向4这个结点；
# 2.然后判断当前当前结点有没有右孩子，如果有右孩子继续入栈，否则将当前结点出栈并记录到结果
# 列表中。然后指针指向出栈的结点的父结点，并修改父结点的左孩子或者右孩子的指针。例如4这个
# 结点没有右孩子，则出栈并且res == [4]，然后指针指向2这个结点并且修改该结点的右孩子指针为
# None。
# 3.当前结点2有右孩子则继续入栈，此时stack == [1, 2, 5]，结点5没有左右孩子则出栈res == [4, 5],
# 并且修改结点2的右孩子指针为None。此时2也没有左右孩子，则res == [4, 5, 2], stack == [1]。
# 4.重复以上操作，直至将根结点出栈。
#