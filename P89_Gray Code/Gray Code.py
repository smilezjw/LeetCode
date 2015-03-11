# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def grayCode(self, n):
        res = []
        for i in xrange(2 ** n):
            res.append(i ^ i >> 1)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.grayCode(3)

##########################################################################################
# 格雷码的生成规则：第一项为0， 下一项toggle（开关，触发）最右边的bit，再下一项toggle最
# 右边值为1的左边一个bit，重复直至最左边的bit为1，其余bit都为0。
# 二进制码和格雷码互相转换规则：
# 1011 = 1（照写第一位） 1（第一位与第二位异或） 1（第二位与第三位异或） 0（第三位与第四位异或）
# 也就是相当于 （1011 >> 1） ^ 1011
# 在python中，可以直接对十进制数进行位运算，也就是代码中先将十进制数i右移一位然后和原来的i进行
# 异或运算。
# 注意题目中n是位数，因此十进制数的范围最大是2**n。