# coding=utf8

__author__ = 'smilezjw'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    if head == None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    start = dummy
    while start.next:
        end = start
        for i in xrange(k-1):  # 注意这里是k-1，所以在reverse中传入的是end.next,这样才有k个结点
            end = end.next
            if end.next == None: # 如果不足k个结点，直接返回链表
                return dummy.next
        # 这里先更新start。next指向的结点，然后更新start指向的结点，这样while循环中start.next是更新后start指向的结点的下一个结点
        (start.next, start) = reverse(start.next, end.next)
    return dummy.next


def reverse(start, end):  # 反转链表k个节点的函数，输入参数为起始结点和尾结点
    dummy = ListNode(0)    # 加入头结点
    dummy.next = start
    while dummy.next != end: # 判断尾结点是否已经反转到头结点的位置
        temp = start.next    #  挨顺序将结点反转到头结点的位置，这里画个图就清楚了
        start.next = temp.next
        temp.next = dummy.next
        dummy.next = temp
    return (end, start)    # 反转后end为头结点，start为尾结点。将反转后的头结点和尾结点返回

if __name__ == '__main__':
    l = ListNode(0)
    head = l
    for i in [1,2,3,4,5]:
        node = ListNode(i)
        head.next = node
        head = head.next
    print reverseKGroup(l.next, 3)

################################################################################################
# 遇到这样复杂的链表指针的题目，头就大了 = = 还是需要画图理清楚思路
# 这道题特别需要搞清楚反转链表结点的函数是如何运作的，并且返回的时候需要更新指针。
#