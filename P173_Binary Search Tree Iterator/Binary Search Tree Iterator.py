# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root):  # 初始化栈用于依次入栈下一个最小的元素
        self.stack = []
        self.pushLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):        # 判断栈是否为空
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):           # 栈顶的节点的值为下一个最小的数字，注意出栈后要将其右孩子节点入栈
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val

    def pushLeft(self, node):  # 将根结点及其右孩子结点依次入栈
        while node:
            self.stack.append(node)
            node = node.left

###################################################################################
# 这道题要求实现一个二叉搜索树的迭代器，迭代器从二叉搜索树的根结点进行初始化，调用
# next()方法会返回二叉搜索树中下一个最小的数字。题目要求next()和hasnext()方法满足
# O(1)时间复杂度，这里用栈来实现。从根节点开始，每次迭代地将根节点及其左孩子入栈，
# 直至左孩子为空。调用next()弹出栈顶，如果被弹出的节点有右孩子，则将右孩子入栈，并
# 将该右孩子节点的左孩子迭代入栈。
#