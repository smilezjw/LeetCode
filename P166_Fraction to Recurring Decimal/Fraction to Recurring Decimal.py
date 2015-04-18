# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        res = ''
        if numerator * denominator < 0:    # 判断结果的正负号
            res = '-'
        if numerator < 0 or denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        integer = numerator / denominator   # 计算结果的整数部分
        numerator -= integer * denominator
        if numerator == 0:                  # 如果能够整除，则余数为0
            res += str(integer)
            return res
        remainder = {}                       # 用来记录余数，已经余数在小数部分出现的位置
        res += str(integer) + '.'
        pos = len(res)
        # 如果余数已经在hash表中出现过，则结果为无限循环小数；如果余数为0表示结果为有限不循环小数
        while numerator not in remainder and numerator != 0:
            remainder[numerator] = pos
            pos += 1
            integer = numerator * 10 / denominator                # 计算这一位的商
            numerator = numerator * 10 - integer * denominator    # 计算这一位的余数
            res += str(integer)
        if numerator in remainder:  # 无限循环小数找到开始循环的位置，用括号表示循环
            return res[:remainder[numerator]] + '(' + res[remainder[numerator]:] + ')'
        return res


if __name__ == '__main__':
    s = Solution()
    print s.fractionToDecimal(-2147483648, -1)
    print s.fractionToDecimal(500, 10)
    print s.fractionToDecimal(22, 7)
    print s.fractionToDecimal(1, 99)
    print s.fractionToDecimal(1, 5)
    print s.fractionToDecimal(2, -9)
    print s.fractionToDecimal(-2, 9)
    print s.fractionToDecimal(2, 9)

###################################################################################################
# 这道题用哈希表来记录小数部分的余数出现的位置，如果再次遇到相同的余数则说明计算结果是无限循环小数，
# 否则当余数为0时则说明计算结果是有限不循环小数。这道题需要注意以下几点：
# 1.注意计算结果的正负号，要先对被除数和除数处理，避免python中除法都是向下取整的问题。
# 2.注意极限的情况，例如-2147483648转化为正数则溢出，所以python自动转换为long int, Long integers have
# unlimited precision in Python.
# 这道题和Divide Two Integers类似。