# coding=utf8

__author__ = 'smilezjw'


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        map = {}
        # 先处理头节点，新建一个节点使其映射到头节点
        newHead = RandomListNode(head.label)
        map[head] = newHead
        # 然后处理头节点的随机链接节点
        if head.random:
            if head.random not in map:
                randNode = RandomListNode(head.random.label)
                newHead.random = randNode
                map[head.random] = randNode
            else:
                newHead.random = map[head.random]
        head = head.next
        p = newHead
        while head:
            if head not in map:  # 判断当前节点是否已经在hash表中，如果是则直接映射，不是则新建节点并映射
                curr = RandomListNode(head.label)
                map[head] = curr
            else:
                curr = map[head]
            p.next = curr
            # 同样的步骤处理当前节点的随机链接节点
            if head.random:
                if head.random not in map:
                    randNode = RandomListNode(head.random.label)
                    curr.random = randNode
                    map[head.random] = randNode
                else:
                    curr.random = map[head.random]
            head = head.next
            p = p.next
        return newHead

if __name__ == '__main__':
    s = Solution()
    head = RandomListNode(1)
    p = head
    p.next = RandomListNode(2)
    p = p.next
    p.random = head
    p.next = RandomListNode(3)
    print s.copyRandomList(head)

###############################################################################################
# 这道题采用了hash表对原来链表中的节点和新构成的链表中的节点一一映射。
# 看网上还有另外一种思路：http://www.cnblogs.com/zuoyuan/p/3745126.html
# 1.在原链表的每个节点后面都插入一个新的节点使得新节点的值和原来节点的值相等；
# 2.原链表中random指针映射方法为：tmp.next.random = tmp.random.next；
# 3.将新的链表从整个构成的链表中拆分出来。
# 个人感觉这种做法感觉很麻烦，没有直接用hash table来的清晰。
#