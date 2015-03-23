# coding=utf8

__author__ = 'smilezjw'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortedListToBST(self, head):
        num = []
        # 遍历链表，将链表中的数字记录下来
        while head:
            num.append(head.val)
            head = head.next
        return self.BST(num)

    def BST(self, num):
        if num == []:
            return None
        medium = len(num) / 2
        # 每次选择数组中间的元素作为父结点，然后该元素左边的元素作为左子树，右边的元素作为右子树
        root = TreeNode(num[medium])
        root.left = self.BST(num[:medium])
        root.right = self.BST(num[medium+1:])
        return root

#######################################################################################
# 这道题采用上一题P108的思路，先遍历链表按递增顺序记录链表中的元素，然后就和P108题一样
# 一样了。
#