# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]  # 初始化第一行
        for n in xrange(1, numRows):
            currLen = len(res[n-1])+1  # 这一行元素的个数比上一行多一个
            curr = [1 for i in xrange(currLen)]  # 初始化这一行的元素
            for i in xrange(1, currLen-1):
                curr[i] = res[n-1][i-1] + res[n-1][i]  # 杨辉三角
            res.append(curr)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.generate(4)

#####################################################################################
# 求解杨辉三角，每一行元素个数都比上一行元素个数多一个，初始化当前行元素为1，然后
# 逐个加法求解。
#