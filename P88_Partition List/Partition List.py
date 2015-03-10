# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        head1 = ListNode(0)  # 头结点，这个链表记录比x小的值的结点
        head2 = ListNode(0)  # 头结点，这个链表记录比x大的值的结点
        curr = head
        phead1 = head1
        phead2 = head2
        while curr:
            if curr.val < x:  # 条件判断的分支其实操作是一样一样的
                phead1.next = curr
                curr = curr.next
                phead1 = phead1.next
                phead1.next = None
            else:
                phead2.next = curr
                phead2 = phead2.next
                curr = curr.next
                phead2.next = None
        phead1.next = head2.next  # 然后把记录比x大的值的链表链接到另一个链表尾部
        return head1.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(0)
    dummy = head
    for i in [2, 1]:
        temp = ListNode(i)
        head.next = temp
        head = head.next
    print s.partition(dummy.next, x=2)

##########################################################################################
# 这道题刚开始尝试原地修改链表，发现不太容易。改为两个链表，分别记录比x小的值的结点和大于
# 等于x的值的结点，然后把大于等于x的值的结点的链表链接到另一个链表的尾部即可。
#