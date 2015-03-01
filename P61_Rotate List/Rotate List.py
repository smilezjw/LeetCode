# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if k == 0:
            return head
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy    # 这里用到两个指针
        length = 0      # 因为k为非负数，因此k可能大于链表程度，需要判断
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = dummy.next     # 将链表首尾相连，这样可以rotate
        k = length - (k % length)  # 倒数第k个则为整数length - k，这里还要判断k和链表长度的关系
        for i in xrange(k):
            curr = curr.next       # 整数length-k个节点后，下一个结点就是rotate起始节点
        head = curr.next
        curr.next = None
        return head

if __name__ == '__main__':
    s = Solution()
    llist = ListNode(0)
    head = llist
    for i in [1, 2, 3, 4, 5]:
        node = ListNode(i)
        head.next = node
        head = head.next
    print s.rotateRight(llist.next, 2).val

#####################################################################################################
# 这道题需要判断k和链表长度的关系。倒数第k个节点可以用正数length - k来表示。
#