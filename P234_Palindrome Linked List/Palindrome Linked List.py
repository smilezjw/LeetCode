# coding=utf8

__author__ = 'smilezjw'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        fast = head
        slow = head
        while fast.next and fast.next.next:  # 首先用快慢指针找到链表中间结点
            fast = fast.next.next
            slow = slow.next
        curr = slow.next
        while curr.next:                     # 用头插法将链表中间结点之后的结点反转
            p = curr.next
            curr.next = p.next
            p.next = slow.next
            slow.next = p
        slow = slow.next
        while slow:                          # 然后前后两部分判断是否相同
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    p = head
    for i in [4, -1, -1, 4, 1]:
        p.next = ListNode(i)
        p = p.next
    print s.isPalindrome(head)

#####################################################################################
# O(n)时间复杂度和O(1)空间复杂度
#
