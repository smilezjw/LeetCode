# coding=utf8

__author__ = 'smilezjw'


class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        # 正向遍历
        for i in xrange(1, n):
            res[i] = res[i-1] * nums[i-1]
        last = 1
        # 反向遍历
        for i in xrange(n-1, -1, -1):
            res[i] *= last
            last *= nums[i]
        return res


if __name__ == '__main__':
    s = Solution()
    print s.productExceptSelf([1, 2, 3, 4])

########################################################################################
# 首先想到的思路是遍历一遍数组计算所有数字的乘积，然后再遍历一遍数组计算除以每一个数字。
# 这种思路需要判断0出现的情况，没有0,0出现一次，0出现多余1次。
# 参考思路非常巧妙： res[i] = (x0 * x1 * ... * xi-1) * (xi+1 * ... * xn-1)
# 第一次正向遍历数组，res[i]中计算x0 - xi-1的乘积；
# 第二次反向遍历，用一个变量保存xi+1 - xn-1的乘积，并且再乘以res[i]就是第i个位置的结果。
