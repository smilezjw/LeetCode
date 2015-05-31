# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        # 如果抢劫第一个房屋，则不能抢劫最后一个房屋；
        # 同样如果抢劫最后一个房屋，则不能抢劫第一个房屋
        # 取这两种情况的最大值
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))


    # 这里复用house robber的代码即可
    def robLinear(self, nums):
        length = len(nums)
        dp = [0 for i in xrange(length+1)]
        dp[1] = nums[0]
        for i in xrange(2, length+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    nums0 = [1]
    nums1 = [2, 1, 1, 2]
    print s.rob(nums0)
    print s.rob(nums1)

##########################################################################################
# 这道题对P198进行扩展，是一道环形动态规划问题，可以通过划分两种情况将其转化为线性动态
# 规划问题。需要考虑的情况两种：如果抢劫第一个房屋，则不能抢劫最后一个房屋；同样如果抢劫
# 最后一个房屋，则不能抢劫第一个房屋。
# 对于每一种情况，计算最大收益可以直接复用P198题的代码即可。
#