# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time Limit Exceeded 时间复杂度为O(n^2)
    def reorderList_ThreePointers(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
        p = head
        while p and p.next:  # p指向插入的位置的前一个节点
            curr = p
            while curr.next and curr.next.next:  # curr指向倒数第二个节点
                curr = curr.next
            q = curr.next  # q指向倒数一个节点
            curr.next = None
            temp = p.next
            p.next = q
            q.next = temp
            p = p.next.next
        return head.next.val

    def reorderList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
        # 使用快慢指针将链表拆分成两个部分：
        # 如果链表长度为奇数则前面的链表比后面的链表长度多1
        # 如果链表长度为偶数则前面的链表比后面的链表长度多2
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # 将第二个链表进行翻转，链表翻转问题
        dummy = ListNode(0)  # 增加一个头结点
        dummy.next = head2
        p = head2.next  # 从第二个链表的第二个结点开始依次翻转
        head2.next = None
        while p:
            temp = p
            p = p.next
            temp.next = dummy.next
            dummy.next = temp
        head2 = dummy.next

        # 归并两个链表
        p = head1
        q = head2
        while q:
            tmp1 = p.next
            tmp2 = q.next
            p.next = q
            q.next = tmp1
            p = tmp1
            q = tmp2
        return head


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    curr = head
    for i in [2, 3, 4, 5, 6]:
        curr.next = ListNode(i)
        curr = curr.next
    print s.reorderList(head)

###########################################################################################
# 一开始自己想的方法时间复杂度为O(n^2)导致超时。
# 看人家的算法主要先将链表差分成两个部分，用快慢指针完成；然后将第二个链表翻转；最后归并
# 两个链表即可。该算法的时间复杂度为O(n)。
# 这道题不仅考了快慢指针，还用到了翻转链表的算法。
#