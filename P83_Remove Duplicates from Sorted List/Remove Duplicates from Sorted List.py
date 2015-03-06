# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        dummy = ListNode(0)  # 构建头结点
        dummy.next = head    # 头结点指向链表
        while head.next:
            if head.val == head.next.val:  # 如果当前结点的值和下一个结点的值相同
                tmp = head.next            # 那么当前结点指向下下一个结点
                head.next = tmp.next
            else:                          # 如果两个相邻结点的值不同（整个链表已经排好序）
                head = head.next           # 那么向后遍历下一个结点
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(0)
    head1 = head
    for i in [1, 1, 2]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    print s.deleteDuplicates(head1.next)

#############################################################################################
# 首先构建一个头结点，让头结点指向链表的第一个结点。然后从链表的第一个结点开始遍历，如果当前
# 结点的值和下一个结点的值相等，则让当前结点指向下下一个结点；否则继续向后遍历下一个结点。
#