# coding=utf8

__author__ = 'smilezjw'

import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists_list(lists):
    i = 0
    while i < len(lists) - 1:  # i和j两个列表两两进行排序
        j = i + 1
        p = 0
        while p < len(lists[i]):
            q = 0
            while q < len(lists[j]):
                if lists[i][p] < lists[j][q]:
                    if q == 0:
                        lists[j].insert(0, lists[i][p])
                        break
                    if q > 0:
                        lists[j].insert(q, lists[i][p])
                        break
                if lists[i][p] > lists[j][q] and q == len(lists[j]) - 1:
                    lists[j].append(lists[i][p])
                q += 1
            p += 1
        lists.remove(lists[i]) # i和j两个列表完成排序后删除掉i，排序结果保留为j
    return lists


def mergeKLists(lists):
    heap = []
    for node in lists:
        if node != None:
            heap.append((node.val, node))
    heapq.heapify(heap)  # 将k个链表的头结点建立最小堆
    head = ListNode(0)   # 初始化保存结果的链表
    curr = head
    while heap:
        pop = heapq.heappop(heap)  # 弹出最小值
        print pop[0]              # pop[0]为最小值
        curr.next = pop[1]         # pop[1]为最小值的那个结点
        curr = curr.next
        if pop[1].next:            # 将链表的下一个结点入堆，并弹出此时堆内的最小值
            heapq.heappush(heap, (pop[1].next.val, pop[1].next))
    return head.next


if __name__ == '__main__':
    #print mergeKLists_list([[11,13,15],[2,4,6],[1,3,5],[0,10,20,50]])
    l1 = ListNode(0)
    head1 = l1
    for i in [2, 4, 6]:
        node1 = ListNode(i)
        head1.next = node1
        head1 = head1.next
    l2 = ListNode(0)
    head2 = l2
    for j in [1, 3, 5]:
        node2 = ListNode(j)
        head2.next = node2
        head2 = head2.next
    l3 = ListNode(0)
    head3 = l3
    for p in [0, 0, 0]:
        node3 = ListNode(p)
        head3.next = node3
        head3 = head3.next
    print mergeKLists([l1.next, l2.next, l3.next])

################################################################################################
# 这道题一开始我直接以列表list的形式，用两两比较的方法将k个排序号的列表进行排序。
# 参考了人家的做法，以前没有接触过python的堆heapq操作，没想到这么方便，和list一样方便。
# 主要思路是首先将k个有序链表的头结点建成最小堆，弹出最小值；然后将链表的下一个结点入堆再弹出
# 最小值，依次操作即可将k个有序链表进行排序。