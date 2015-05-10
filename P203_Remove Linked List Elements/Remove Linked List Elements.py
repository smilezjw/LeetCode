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

    def removeElements_II(self, head, toBeDeleted):
        if not head:
            return head
        if toBeDeleted.next:
            nextNode = toBeDeleted.next
            toBeDeleted.val = nextNode.val
            toBeDeleted.next = nextNode.next
            del nextNode
        elif head == toBeDeleted:
            head = None
        else:
            p = head
            while p.next != toBeDeleted:
                p = p.next
            p.next = None
        return head


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

    head = ListNode(1)
    p = head
    for i in [2, 3, 4, 5, 6]:
        p.next = ListNode(i)
        p = p.next
    toBeDeleted = head.next.next
    # print s.removeElements_II(head, p)
    print s.removeElements_II(head, toBeDeleted)

    head2 = ListNode(1)
    print s.removeElements_II(head2, head2)


#####################################################################################
# 题目比较简单，建立头节点，并用指针p来遍历链表，p.next判断节点是否要删除，这样p指向
# 要删除的节点的前一个节点。注意只有当判断p.next不是要删除的节点时，再移动p指针，避免
# 连续节点都要被删除。
# 根据剑指Offer中要求在O(1)时间删除链表结点，假设要删除结点i，先把i的下一个结点j的内
# 容复制到i，然后把i的指针指向结点j的下一个结点，此时再删除结点j，其效果正是把结点i
# 给删除了。如果要删除的结点位于链表的尾部，则只能从链表头结点开始，顺序遍历得到该结点
# 的前序结点完成删除操作。如果链表中只有一个结点，需要在删除之后把链表的头结点置为None。
# 这种方法基于假设要删除的结点在链表中。
# 第一种方法是删除具有val的结点，因此可能多个结点都具有val值，第二种方法则不存在删除多个
# 结点的情况。
#