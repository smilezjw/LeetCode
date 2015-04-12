# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, head1, head2):  # 对两个链表进行归并排序
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        dummy = ListNode(0)
        p = dummy
        while head1 and head2:
            if head1.val < head2.val:
                p.next = head1
                p = p.next
                head1 = head1.next
            else:
                p.next = head2
                p = p.next
                head2 = head2.next
        if head1 is None:
            p.next = head2
        if head2 is None:
            p.next = head1
        return dummy.next

    def sortList(self, head):  # 这里将一个链表拆分成两个链表
        if head is None or head.next is None:
            return head
        slow = fast = head
        while fast.next and fast.next.next:  # 使用快慢指针来截断链表，注意这里的循环停止条件，避免出现死循环
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None  # 注意截断链表时将前半部分的链表最后一个节点next指针指向None
        head1 = self.sortList(head1)  # 递归对head1链表进行排序
        head2 = self.sortList(head2)  # 递归对head2链表进行排序
        return self.merge(head1, head2)

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    p = head
    for i in [3, 2, 5]:
        p.next = ListNode(i)
        p = p.next
    print s.sortList(head)

###################################################################################################
# 这道题参考网上都采用归并排序，归并排序最坏情况下时间复杂度为O(nlogn),空间复杂度为O(n)。
# 这里是对一个链表进行归并排序，因此需要将该链表截断为两部分，并递归分别对两部分链表进行排序，最后
# 才对两部分链表进行归并排序。尤其需要注意：
# 1.截断两个链表时的快慢指针技巧，已经截断后前一部分最后一个节点的next指针指向None;
# 2.需要递归对两部分链表进行排序，不要截断完直接对两部分链表排序就错了。
#