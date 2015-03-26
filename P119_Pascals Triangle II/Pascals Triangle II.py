# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        value = [1]
        for k in xrange(1, rowIndex+1):
            curr = [1 for i in xrange(k+1)]
            for i in xrange(1, k):
                curr[i] = value[i-1] + value[i]
            value = curr[:]  # 注意这里是分片赋值
        return value

if __name__ == '__main__':
    s = Solution()
    print s.getRow(0)
    print s.getRow(1)
    print s.getRow(2)
    print s.getRow(5)

###################################################################################
# 这道题的思路和上一题类似，只是为了use only O(k) extra space, 这里采用分片赋值的
# 方法仅保留每一行的结果，然后下一行根据上一行的结果进行结算。
#