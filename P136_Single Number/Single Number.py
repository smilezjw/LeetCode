# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def singleNumber(self, A):  # 自己的写法就这这么low
        if len(A) == 1:
            return A[0]
        A.sort()
        for i in xrange(1, len(A)-1):
            if A[i-1] < A[i] < A[i+1]:
                return A[i]
        if A[0] < A[1]:
            return A[0]
        if A[-1] > A[-2]:
            return A[-1]

    def singleNumber_bitManipulation(self, A):  # 这种解法使用位操作
        ans = A[0]
        # 对于唯一的那个数，之前的异或操作都清零了，之后的异或操作结合律也都清零了
        for i in xrange(1, len(A)):
            ans ^= A[i]
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1, 1, 2, 3, 3])

######################################################################################
# 这道题主要考位操作： 使用异或， x ^ 0 = x, x ^ x = 0
#