# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        q = p.next
        length = 0
        while q.next:  # 判断每次从dummy结点到q的距离是否增大了，如果不是递增则说明有环
            curr = p
            count = 0
            while curr != q:
                count += 1  # count记录从dummy结点到q结点的距离
                curr = curr.next
            print count
            if count <= length:  # 如果距离不是递增的，则说明出现环
                return True
            length = count
            q = q.next
        return False

    def hasCycle_TwoPointers(self, head):
        if head is None or head.next is None:
            return False
        slow = fast = head    # 快、慢指针初始都指向头结点
        while fast and fast.next:  # 如果没有环，则快指针fast或者fast.next首先指向None
            slow = slow.next        # 慢指针每次只走一步
            fast = fast.next.next   # 快指针每次走两步
            if slow == fast:        # 如果有环，则总有快慢指针指向同一个结点的时候
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    p = head
    for i in [2, 0, 4]:
        p.next = ListNode(i)
        p = p.next
    p.next = head.next
    head2 = ListNode(1)
    head2.next = head2
    print s.hasCycle_TwoPointers(head)

###########################################################################################
# 这道题一开始想用从dummy结点到q指针指向的结点之间的距离是否一直在递增来判断是否出现环，
# 但是这种思路会超时，时间复杂度为O(n^2)。
# 看人家用了快、慢两个指针，快指针每次走两步，慢指针每次走一步，如果没有环则fast或者
# fast.next首先指向None，否则快慢指针会有一个时刻指向同一个结点。挺巧妙的思路。
#