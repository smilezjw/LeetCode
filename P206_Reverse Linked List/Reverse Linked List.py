# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 头插法，画个图逐个结点走一遍
    def reverseList_Iterative(self, head):
        if not head:    # 如果链表为空直接返回
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy.next
        while p.next:
            q = p.next
            p.next = q.next
            q.next = dummy.next
            dummy.next = q
        return dummy.next.val


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    print s.reverseList_Iterative(head)

    head2 = ListNode(1)
    p = head2
    p.next = ListNode(2)
    print s.reverseList_Iterative(head2)

#################################################################################
# 用头插法求解反转链表的问题还是很经典的。
#