# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        for i in xrange(1, m):  # prev指向第m个结点前面的那个结点
            prev = curr         # curr指向第m个结点
            curr = curr.next
        p1 = ListNode(0)
        p2 = ListNode(0)        # 初始化p1和p2，p1和p2可能为空
        if curr:
            p1 = curr.next      # p1指向第m个结点后面的那个结点， p1可能为空
        if p1:
            p2 = p1.next        # p2指向第m个结点后面的第2个结点
        for i in xrange(m, n):  # 每次反转相邻两个结点的链接，并且顺序移动三个指针
            p1.next = curr      # 循环结束时curr指向第n个结点
            curr = p1
            p1 = p2
            if p2:
                p2 = p2.next
        prev.next.next = p1     # 原来第m个结点链接到p1，p1现在指向第n个结点后面一个结点
        prev.next = curr        # 原来第m个结点的前一个结点链接到第n个结点，同时完成链表的反转
        return dummy.next

################################################################################################
# 这道题需要用到三个指针，依次从第m个结点到第n个结点两两反转，最后处理第m个链接到第n个结点后面
# 一个结点，并且第m个结点的前一个结点链接到第n个结点。画画图会更加清晰。
#