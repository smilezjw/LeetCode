# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def rob(self, num):
        length = len(num)
        if length == 0:
            return 0
        # dp[i]表示打劫到第i个房子时累计获得的金钱最大值
        dp = [0 for i in xrange(length+1)]
        dp[1] = num[0]
        for i in xrange(2, length+1):
            # 状态转移方程，有两种状态：第i-1房屋如果没有打劫，以及第i-1房屋被打劫了
            dp[i] = max(dp[i-1], dp[i-2] + num[i-1])
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    num = [2, 1, 1, 2]
    print s.rob(num)

#######################################################################################
# 这道动态规划的题目还是比较容易想到的，一般构造一维的状态转移方程的动态规划题目还是相
# 对容易考虑得到的。
#