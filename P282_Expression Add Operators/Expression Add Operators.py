# coding=utf8

__author__ = 'smilezjw'


class Solution(object):
    def addOperators(self, num, target):
        res = []
        self.helper(num, target, '', 0, 0, res)
        return res

    def helper(self, num, target, tmp, currRes, prevRes, res):
        if currRes == target and len(num) == 0:  # 搜索到一种解
            res.append(tmp)
            return
        for i in xrange(1, len(num)+1):  # 遍历数字拆分情况
            currStr = num[:i]
            if len(currStr) > 1 and currStr[0] == '0':  # 如果是00,01等以0为开头的情况，则直接返回
                return
            currNum = long(currStr)  # 由于数字可能超出int表示的范围，因此用long来表示
            # 如果是2+3*4，则对于2+3的结果，要变成（5-3）+ 3 * 4，所以用currRes记录上一次计算的结果，prevRes记录上一次计算用到的值
            # 如果是2+3*4*5，则变成（14-12）+ 12 * 5 = 62, 也是一样的
            if len(tmp) > 0:
                self.helper(num[i:], target, tmp+'+'+currStr, currRes + currNum, currNum, res)
                self.helper(num[i:], target, tmp+'-'+currStr, currRes - currNum, -currNum, res)  # 注意这里的负号
                self.helper(num[i:], target, tmp+'*'+currStr, (currRes - prevRes) + prevRes * currNum, prevRes * currNum, res)
            else:
                self.helper(num[i:], target, currStr, currNum, currNum, res)


if __name__ == '__main__':
    s = Solution()
    print s.addOperators('123', 6)
    print s.addOperators('232', 8)
    print s.addOperators('105', 5)
    print s.addOperators('000', 0)
    print s.addOperators('3456237490', 9191)


########################################################################################
# 因为要输出所有的可能性，所以用深度优先搜索。因为数字可以是个位数，或者是两位数等，因此
# 外层循环还要遍历数字的拆分情况。
# 我们需要如下变量：currRes记录上一次计算结果的值，prevNum记录上一次用于计算的操作数的值，
# currNum是当前准备进行计算的操作数的值， currStr则是currNum的字符串形式， temp记录目前
# 为止的运算过程的字符串形式。
#