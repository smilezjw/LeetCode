# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        if head is None:
            return None
        dummy = ListNode(0)  # 添加一个头节点
        dummy.next = head
        curr = head
        while curr.next:
            if curr.val > curr.next.val:  # 如果链表的相邻节点是升序的，则curr指针一直向后移动
                pre = dummy               # 否则从头节点开始，找到一个节点的值小于curr.next的值即找到插入的位置
                while pre.next.val < curr.next.val:
                    pre = pre.next
                temp = curr.next          # 进行插入操作
                curr.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                curr = curr.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    p = head
    for i in [3, 2, 5]:
        p.next = ListNode(i)
        p = p.next
    print s.insertionSortList(head)

#####################################################################################################
# 插入排序在最坏情况下时间复杂度为O(n)。
#
