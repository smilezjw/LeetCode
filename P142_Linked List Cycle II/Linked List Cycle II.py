# coding=utf8

__author__ = 'smilezjw'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:  # 判断有环
                break
        if fast == slow:
            slow = head
            while slow != fast:  # 找到环的起点
                slow = slow.next
                fast = fast.next
            return slow.val
        return None

if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    p = head
    for i in [2, 0, 4]:
        p.next = ListNode(i)
        p = p.next
    p.next = head.next
    head2 = ListNode(0)
    head2.next = head2
    print s.detectCycle(head)

############################################################################################
# 对于这道题目，我只能说奥数题目大概就是这样计算的。
# 具体示意图参考：http://www.cnblogs.com/zuoyuan/p/3701877.html
# 从head到环路起点距离为K，起点到fast和slow的相遇点距离为M，整个环路周长为L。假设当fast和
# slow相遇时，fast走过了Lfast，slow走过了Lslow，根据题意可知：
# Lslow = K + M
# Lfast = K + M + n * L
# Lfast = 2 * Lslow
# 根据上面三个式子可以得出： K = n * L - M = (n - 1) * L + L - M
# 将slow重新从head开始，fast从相遇点开始走，每次都只走一步，slow走了K步到达环的起点，此时fast
# 绕着环走了n-1圈，并且也到达了环的起点。于是，环的起点通过再次判断fast == slow就找到了。
# 这样不需要具体计算K、L、M距离的值，通过两次判断slow == fast即可判断是否有环以及环的起点。
#