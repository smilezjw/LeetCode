# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        for i in xrange(1, len(prices)):
            # 判断是否是递增序列，递增则可以在最低点买入，最高点抛出，得到这一时间段内最大利润
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit

if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([1, 2, 3, 5])

################################################################################
# 这道题采用贪心法的思想，找出数组中所有递增序列，递增序列表示可以在最低点买入，
# 最高点卖出，得到这一时间段内的最大利润。如果是递减序列则观望不进行交易。
# 实际上是不可能这样操作的。
#