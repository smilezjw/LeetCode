# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Memory Limit Exceeded
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        node = {}
        p = headA
        # 首先遍历headA链表，将其结点都映射到hash表中
        while p:
            node[p] = True
            p = p.next
        q = headB
        while q:
            # 遍历headB链表，如果结点已经在hash表中，则找到交点了
            if q in node:
                return q
            q = q.next
        return None

    # 计算链表长度
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # 使用双指针，计算两个链表的长度差，
    # 然后长链表先走长度差的步数，然后再两个指针一起走直到遇到交点或者链尾
    def getIntersectionNode_TwoPointers(self, headA, headB):
        if headA is None or headB is None:
            return None
        p = headA
        q = headB
        lenA = self.getLength(p)
        lenB = self.getLength(q)
        if lenA > lenB:
            long = headA
            short = headB
        else:
            long = headB
            short = headA
        # 计算两个链表的长度差
        distance = abs(lenA - lenB)
        # 指向长链表的指针先走长度差的步数
        for i in xrange(distance):
            long = long.next
        # 长短链表指针一起走
        while long and short:
            # 找到交点
            if long == short:
                return short
            long = long.next
            short = short.next
        return None


if __name__ == '__main__':
    s = Solution()
    headA = ListNode(1)
    p = headA
    for i in [2, 3, 4, 5]:
        p.next = ListNode(i)
        p = p.next
    headB = ListNode(6)
    q = headB
    q.next = headA.next
    print s.getIntersectionNode(headA, headB)
    print s.getIntersectionNode_TwoPointers(headA, headB)

########################################################################################
# 这道题可以有多种解题思路：
# 1.暴力搜索：遍历链表A的所有节点，并且对于每个节点都与链表B中的所有结点比较。时间复杂度
# 为O(lenA * lenB), 空间复杂度为O(1)。
# 2.哈希表：遍历链表A，将A的所有节点存入哈希表中，然后遍历链表B，对于B中的每个结点查找哈希
# 表，如果在哈希表中找到则说明是两个链表的交点。时间复杂度为O(lenA + lenB), 空间复杂度为
# O(lenA)或者O(lenB)。
# 3.双指针法：分别计算链表A和B的长度，计算两者的长度差，然后用两个指针分别指向两个链表的
# 首节点，长链表指针首先走长度差那么多步，然后两个指针一起走，当两个指针指向的节点相同时
# 即找到交点。时间复杂度为O(lenA + lenB)，空间复杂度为O(1)。
#