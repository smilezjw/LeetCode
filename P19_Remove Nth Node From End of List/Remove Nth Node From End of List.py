# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    p1, p2 = dummy, dummy  # 双指针
    for i in xrange(n):   # p1先移动n个节点
        p1 = p1.next
    while p1.next:        # 这里利用的还是倒数第n个节点 = 第列表长度减去n个节点
        p1 = p1.next       # p1到达链表末尾
        p2 = p2.next       # p2和p1相差n个节点，此时p2指向的节点正是要删除的节点
    p2.next = p2.next.next
    return dummy.next

if __name__ == '__main__':
    llist = ListNode(0)
    head = llist
    for i in [1, 2, 3, 4, 5]:
        node = ListNode(i)
        head.next = node
        head = head.next
    print removeNthFromEnd(llist.next, 2)

#############################################################################################
# 一遍扫描即可找到链表倒数第n个节点删除掉，利用双指针，首先加一个头结点，p1先向前移动n个节点，
# 然后p1和p2同时向前移动， 当p1到达链表最后一个节点时，p1.next == None, 此时p2指向的正是要删除
# 的节点。真是太机智了！！！
#