# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # Time limit exceeded
    # O(n)时间复杂度
    def rangeBitwiseAnd(self, m, n):
        if m == 0:
            return 0
        res = m
        for i in xrange(m+1, n+1):
            res &= i
        return res

    # [m, n]范围的位与操作的结果是m和n的公共左边的位
    def rangeBitwiseAnd_accepted(self, m, n):
        offset = 0
        while m != n:
            m >>= 1
            n >>= 1
            offset += 1
        return n << offset

if __name__ == '__main__':
    s = Solution()
    print s.rangeBitwiseAnd(0, 2**31-1)
    print s.rangeBitwiseAnd(1, 5)
    print s.rangeBitwiseAnd(5, 7)
    print s.rangeBitwiseAnd_accepted(0, 2**31-1)
    print s.rangeBitwiseAnd_accepted(1, 5)
    print s.rangeBitwiseAnd_accepted(5, 7)

#####################################################################################
# 这道题如果用O(n)时间复杂度去位与计算则会超时，从数学角度考虑，得出规律：# [m, n]
# 范围的位与操作的结果是m和n的左边公共的位。如5(101)和7(111)，则左边公共的位为1，通过
# 右移两位判断得出，因此将左边公共的位1再左移两位即可得到位与的结果100—4。
#