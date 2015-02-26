# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 用数学的方法解题，相当于C(m-1+n-1, m-1) == C(m-1+n-1, n-1)
    def uniqePaths(self, m, n):
        N = m - 1 + n - 1
        K = m - 1
        res = 1
        for i in xrange(1, K+1):
            res = res * (N-i+1) / i
        return res

if __name__ == '__main__':
    s = Solution()
    print s.uniqePaths(3, 3)

##########################################################################################
# 用组合数学的方法结题，相当于相当于C(m-1+n-1, m-1) == C(m-1+n-1, n-1)
#