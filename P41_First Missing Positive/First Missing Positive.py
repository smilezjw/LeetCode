# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def firstMissingPositive(self, A):
        if len(A) == 0:
            return 1
        A.sort()
        temp = 0
        for i in xrange(len(A)):
            if A[i] <= 0:
                continue
            # 从1开始，如果出现1则开始累加判断连续正数；如果没有出现1则返回1
            if A[i] - temp == 1:
                temp += 1
        return temp + 1

if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([3, 4, -1, 1])
    print s.firstMissingPositive([1, 2, 0])
    print s.firstMissingPositive([1])

############################################################################################
# 这道题和其他人的作法不一样，参考其他人的做法是交换元素，看上去很复杂；
# 我虽然引入变量temp，但是很简单的思路，判断1是否出现：出现1则开始累加计数看接下去哪个正数
# 没有出现；否则就返回1。这种思路只需要扫描一遍列表，但是不知道这样引入变量是否符合
# constant space的要求。