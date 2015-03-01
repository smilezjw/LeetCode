# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def sqrt(self, x):  # Implement int sqrt(int x)
        i = 0
        j = x / 2 + 1    # 二分查找的终点为x / 2 + 1, 因为(x / 2 + 1) ^ 2 > x
        while i <= j:
            mid = (i + j) / 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                j = mid - 1
            else:
                i = mid + 1
        return j  # 如果x开方的结果不是整数，那么返回整数部分，注意这里应该返回j

if __name__ == '__main__':
    s = Solution()
    print s.sqrt(9)
    print s.sqrt(2)

######################################################################################################
# 因为这道题要求开方的结果是整数，所以考虑用二分查找的方法来求解。注意二分查找的起点为0，终点为
# x / 2 + 1, 还要主要如果开方的结果不是一个整数，那么返回其整数部分，搞清楚代码里应该返回i还是返回j。
#