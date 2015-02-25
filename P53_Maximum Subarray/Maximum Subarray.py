# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def maxSubArray(self, A):
        subSum = 0
        maxSum = -2**31
        for i in xrange(len(A)):
            if subSum < 0:  # 如果累加和已经小于0，那么还不如不加，所以这时候从新开始
                subSum = 0
            subSum += A[i]  # 如果全是负数的话，其实就是选择负数中的最大的一个数
            maxSum = max(maxSum, subSum)
        return maxSum

if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

##########################################################################################
# 这道题看上去很复杂，但是代码却非常简洁明了：从第0个数字开始累加，如果累加和小于0，那么还
# 不如不加，所以重新开始；如果全都是负数，其实就是选择负数中最大的一个数。
#