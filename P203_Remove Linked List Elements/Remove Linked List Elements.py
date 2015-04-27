# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:  # 这里如果p.next.val != val，再移动指针p，避免连续两个节点的值都等于val
                p = p.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    p = head
    for i in [2, 6, 3, 4, 5, 6]:
        p.next = ListNode(i)
        p = p.next
    head2 = ListNode(1)
    head2.next = ListNode(1)
    print s.removeElements(head, 6)
    print s.removeElements(head2, 1)

#####################################################################################
# 题目比较简单，建立头节点，并用指针p来遍历链表，p.next判断节点是否要删除，这样p指向
# 要删除的节点的前一个节点。注意只有当判断p.next不是要删除的节点时，再移动p指针，避免
# 连续节点都要被删除。
#