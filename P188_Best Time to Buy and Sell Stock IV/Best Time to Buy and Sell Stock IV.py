# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def maxProfit(self, k, prices):
        length = len(prices)
        # 如果最大交易次数大于len(prices) / 2， 则题目转化为可以任意次数交易(该系列第二题II)
        if k > (length / 2):
            return self.maxProfitNoLimit(prices)
        # 初始化状态转移方程，注意负实数 > None
        dp = [None] * (2 * k + 1)
        dp[0] = 0
        for i in xrange(length):
            for j in xrange(1, min(2*k, i+1)+1):  # 因为i是从0开始计数的，所以这里i+1
                # 当j为奇数时，交易类型为买进；
                # 当j为偶数时，交易类型为卖出；
                # 其实是将prices[i]尝试当做交易序列中的每一个交易步骤j，记录prices[i]当做j步骤时所获得的最大收益
                dp[j] = max(dp[j], dp[j-1] + prices[i] * [1, -1][j % 2])
        # 买入和卖出一共是k*2个交易步骤
        return dp[k*2]

    def maxProfitNoLimit(self, prices):  # 这里的解法就是Best Time to Buy and Sell Stock II中的解法
        maxProfit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit

if  __name__ == '__main__':
    s = Solution()
    print s.maxProfit(2, [1, 2])
    print s.maxProfit(2, [2, 5, 7, 2, 4, 9])
    print s.maxProfit(3, [1,2,4,2,5,7,2,4,9,0])

#########################################################################################
# 这道题比较难，用动态规划做也不太好理解，程序走了几遍才大概清楚。
# 这道题的实质是从长度为len(prices)的数组中挑选出至多k*2个元素组成一个交易序列。交易序列
# 首次买入，然后卖出和买入交替进行。当j为奇数时，交易类型为买入；当j为偶数时，交易类型为
# 卖出。
# 当最大交易次数大于len(prices) / 2时，问题就转化为任意多次交易。
# 遍历数组中每一个元素，将其尝试当做交易序列中每一个交易步骤，取该步骤的最大值。