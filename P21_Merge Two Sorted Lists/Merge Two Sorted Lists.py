# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        curr = ListNode(0)  # 头结点
        dummy = curr
        while l1 and l2:  # 主要循环条件
            if l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        if l2 is None:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(0)
    head = l1
    for i in [1, 3, 5, 7, 9]:
        node = ListNode(i)
        head.next = node
        head = head.next
    l2 = ListNode(0)
    head = l2
    for i in [2, 4, 6, 8]:
        node = ListNode(i)
        head.next = node
        head = head.next
    print s.mergeTwoLists(l1.next, l2.next).val

#####################################################################################################
# 这道题注意循环条件是while l1 and l2, 然后判断两个结点的值的大小，移动指针。第23题是k个有序列表，
# 则不是这么简单操作。
#