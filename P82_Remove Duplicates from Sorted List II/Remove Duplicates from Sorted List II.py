# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        dummy = ListNode(0)  # 构建头结点
        dummy.next = head
        temp = dummy         # 两个指针指向头结点
        flag = False         # flag用来表示该结点的值是否重复
        while head.next:
            # 如果相邻两个结点的值重复，那么flag = True, 并且指针head指向下下个结点
            if head.val == head.next.val:
                flag = True
                head.next = head.next.next
            # 如果相邻两个结点的值不相等，并且flag==False表示head指向的这个值没有重复值，那么temp指向该结点
            elif head.val != head.next.val and not flag:
                temp.next = head
                temp = temp.next
                head = head.next
            # 如果相邻两个结点的值不相等，但是flag == False表示head指向的这个值已经出现过了，那么head指向下一个结点，并且重置flag为False
            else:
                head = head.next
                flag = False
        # 对于最后一个结点来说，如果head指向最后一个结点时flag==False，则该结点没有重复值，temp指向该结点
        if not flag:
            temp.next = head
        # 否则temp指向None
        else:
            temp.next = None
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(0)
    head1 = head
    for i in [1, 2, 2]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    print s.deleteDuplicates(head1.next)

#################################################################################################
# 这道题和第83的题区别是，这道题要求如果保留所有没有重复值的结点；而83题的要求是将所有值保留一个
# 去掉其他重复的结点。这里引入变量flag来表示当前head指向的结点是否有重复值。如果相邻两个结点相等，
# 则flag为True，并且head指向的结点链接到下下个结点；如果相邻两个结点的值不相等，但是flag为True，
# 说明head指向的结点的值出现过重复值，那么head指向下一个结点，flag重新置为false；如果相邻两个结点
# 的值不相等，并且flag为False，说明head指向的结点的值没有出现重复值，那么从头结点出发的temp指针指向
# 该结点，并且head指向下一个结点；如果head指向最后一个结点时（此时跳出while循环），flag为False，说明
# 最后一个结点的值没有重复值，那么temp链接到该结点；否则temp链接到None。
#