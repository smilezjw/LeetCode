# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    if head == None or head.next == None:
        return head
    dummy = ListNode(0)  # 加一个头结点
    dummy.next = head
    prev = dummy         # 采用3个指针，分别指向3个连续的结点
    curr = prev.next
    succ = curr.next
    while curr and succ:
        curr.next = succ.next  # 交换两个结点的3步操作
        succ.next = curr
        prev.next = succ
        if curr.next:         # 更新3个指针，分别向后移动2个节点
            prev = curr
            curr = prev.next
            succ = curr.next
        else:
            break
    return dummy.next

if __name__ == '__main__':
    l = ListNode(0)
    head = l
    for i in [1,2,3,4]:
        node = ListNode(i)
        head.next = node
        head = head.next
    print swapPairs(l.next)

##############################################################################################
# 一开始做这道题目，看到“use only constant space”，以为不能引入新的指针，于是很困扰如何
# 交换两个结点。后来一看人家的代码都是引入多个指针，于是就大胆引入3个指针，分别指向连续的
# 三个结点。这样草稿纸上画一画图，感觉简单了很多。
#
#