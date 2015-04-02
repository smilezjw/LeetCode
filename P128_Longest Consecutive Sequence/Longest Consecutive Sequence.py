# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def longestConsecutive(self, num):
        if num == []:
            return 0
        num.sort()  # 首先当然是排序啦
        maxLength = 0
        tempLen = 0
        for i in xrange(1, len(num)):
            if num[i] - num[i-1] == 1:  # 如果相邻两个数是连续递增的，则tempLen+1
                tempLen += 1
            elif num[i] - num[i-1] > 1:  # 如果相邻两个数递增，但不连续，则tempLen重新置为0
                tempLen = 0
            # 如果相邻两个数相等，则tempLen不变
            maxLength = max(maxLength, tempLen)
        return maxLength+1

if __name__ == '__main__':
    s = Solution()
    print s.longestConsecutive([1, 2, 0, 1])
    print s.longestConsecutive([0, -1])
    print s.longestConsecutive([6, 7, 8, 9, 100, 10, 4, 200, 1, 3, 2])

########################################################################################
# 这道题比较简单，首先排好序，然后主要考虑相邻两个数之间的三种情况：
# 1.相邻两个数连续递增； 2.相邻两个数递增但不连续； 3.相邻两个数相等。
#