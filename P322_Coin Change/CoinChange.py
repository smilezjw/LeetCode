# coding=utf8

class Solution(object):
    def coinChange(self, coins, amount):
        MAX_INT = 2 ** 32 - 1
        dp = [0] + [MAX_INT] * amount
        for i in xrange(1, amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i-j]+1, dp[i])
        if dp[amount] == MAX_INT:
            dp[amount] = -1
        return dp[amount]


if __name__ == '__main__':
    coins = [1,3,5]
    s = Solution()
    print s.coinChange(coins, 11)


##############################################################################
# 动态规划：状态转移方程 dp[i] = min{dp[i-j]+1, dp[i]}， 其中i为amount，j为硬币的面值。
# dp[i]表示凑满金额i所需的最少硬币数。硬币个数不限。
# 参考链接：http://blog.csdn.net/wdxin1322/article/details/9501163
