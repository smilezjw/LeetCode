# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        low = prices[0]
        maxProfit = 0
        for i in xrange(len(prices)):  # 扫描一遍数组
            if prices[i] < low:        # 更新最低的价位
                low = prices[i]
            # 因为只完成依次买进卖出的交易，因此只需要找到当前价格减去到目前为止的最低价就是最高利润
            maxProfit = max(maxProfit, prices[i] - low)
        return maxProfit

if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([1, 2])

##################################################################################
# 这道题目的要求是最多完成一次买入卖出的交易，因此一遍扫描数组，更新最低的价位作
# 为买入价位，然后用当前价位减去当前最低买入价位，取得最大差值就是最大利润。
#