# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        if length == 0:
            return 0
        # 开辟两个数组， f1[i]表示在prices[i]之前进行一次交易所获得的最大利润
        # f2[i]表示在prices[i]之后进行一次交易所获得的最大利润
        f1 = [0 for i in xrange(length)]
        f2 = [0 for i in xrange(length)]
        minPrice = prices[0]
        f1[0] = 0
        for i in xrange(1, length):
            # 找到目前为止的最低价买入
            minPrice = min(minPrice, prices[i])
            f1[i] = max(f1[i-1], prices[i] - minPrice)

        maxPrice = prices[-1]
        f2[-1] = 0
        for i in xrange(length-2, -1, -1):
            # 找到当前价格之后的最高价格卖出
            maxPrice = max(maxPrice, prices[i])
            f2[i] = max(f2[i-1], maxPrice-prices[i])

        maxProfit = 0
        for i in xrange(length):
            maxProfit = max(maxProfit, f1[i] + f2[i])
        return maxProfit

if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([1,2])
    print s.maxProfit([2,1])
    print s.maxProfit([1,2,4,2,5,7,2,4,9,0])
    print s.maxProfit([1,2,3,2,5,6,9,1,2])

#########################################################################################
# 这道题的思路感觉从P121 最多一次交易所能带来的收益那道题的思路类似。
# 这道题需要开辟两个数组，分别正向和反向扫描prices列表，记录在当前价格之间进行交易的最大
# 利润，以及在当前价格之后进行交易的最大利润。时间复杂度为O(n)。
# 使用动态规划思路。
#