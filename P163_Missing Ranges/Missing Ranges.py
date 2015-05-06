# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def missingRanges(self, num, lower, upper):
        length = len(num)
        res = []
        # 当数组为空时，判断upper和lower的关系
        if length == 0:
            if upper > lower:
                res.append(str(lower) + '->' + str(upper))
            else:
                res.append(str(lower))
            return res
        # 判断lower和num[0]的大小关系，对lower -> num[0]之间的值进行处理
        elif lower < num[0]:
            if num[0] - lower == 1:
                res.append(str(lower))
            else:
                res.append(str(lower) + '->' + str(num[0]-1))
        # 由于数组的数字一定是在lower和upper的区间内的,就判断每两个数字之间的间隔
        for i in xrange(0, length-1):
            if num[i+1] - num[i] == 2:
                res.append(str(num[i]+1))
            elif num[i+1] - num[i] > 2:
                res.append(str(num[i]+1) + '->' + str(num[i+1]-1))
            else:
                continue
        # 然后再判断num[-1]和upper的大小关系
        if upper > num[-1]:
            if upper - num[-1] == 1:
                res.append(str(upper))
            else:
                res.append(str(num[-1]+1) + '->' + str(upper))
        return res

if __name__ == '__main__':
    s = Solution()
    num0 = []
    num1 = [0, 1, 3, 50, 75]
    print s.missingRanges(num0, 1, 10)
    print s.missingRanges(num0, 0, 0)
    print s.missingRanges(num1, 0, 99)
    print s.missingRanges(num1, -1, 75)

    num2 = [2]
    print s.missingRanges(num2, 2, 2)

######################################################################################
# 不能提交都不知道能不能过测试集。
# 题目：Given a sorted integer array where the range of elements are [lower, upper]
# inclusive, return its missing range.
# 这道题主要考虑各个数字之间的大小关系：
# 1.如果数组为空，则考虑lower和upper之间的大小关系；
# 2.考虑lower和num[0]的大小关系；
# 3.考虑num[i]和num[i+1]的大小关系；
# 4.考虑num[-1]和upper的大小关系。
#