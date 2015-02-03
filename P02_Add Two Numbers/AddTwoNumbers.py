#_*_ coding:utf8 _*_

__author__ = 'smilezjw'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        flag = 0
        head = dummy
        while flag or l1 or l2:
            node = ListNode(flag)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            flag = node.val / 10      # 需要进位则将进位的数字加到后面的节点上
            node.val = node.val % 10  # 仅保留一位数字
            head.next = node
            head = head.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(0)
    head = l1
    for i in [2,4,3]:
        node = ListNode(i)
        head.next = node
        head = head.next
    l2 = ListNode(0)
    head2 = l2
    for j in [5, 6, 4]:
        node2 = ListNode(j)
        head2.next = node2
        head2 = head2.next
    sol = Solution()
    print sol.addTwoNumbers(l1.next,l2.next)


##################################################################################################
# 这道题涉及到链表数据结构，自己真的不太会写，参考了网上的答案。
# 需要注意的是，这道题目中有一个tricky的地方，就是相加后仅保留一位数字，进位需要加到后面的节点上。
# 主要还是链表数据结构的操作。