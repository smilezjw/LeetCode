# coding=utf8

__author__ = 'smilezjw'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


#####################################################################################
# 链表基本操作，删除结点node，将下一个结点的值赋给当前结点，然后当前结点的下一个结点
# 指向下下个结点，完事了。
#