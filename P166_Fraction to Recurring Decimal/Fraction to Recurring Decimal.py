# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        res = ''
        if numerator * denominator < 0:
            res = '-'
        if numerator < 0 or denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        integer = numerator / denominator
        numerator -= integer * denominator
        if numerator == 0:
            res += str(integer)
            return res
        remainder = {}
        res += str(integer) + '.'
        pos = len(res)
        while numerator not in remainder and numerator != 0:
            remainder[numerator] = pos
            pos += 1
            integer = numerator * 10 / denominator
            numerator = numerator * 10 - integer * denominator
            res += str(integer)
        if numerator in remainder:
            return res[:remainder[numerator]] + '(' + res[remainder[numerator]:] + ')'
        return res


if __name__ == '__main__':
    s = Solution()
    print s.fractionToDecimal(-2147483648, 1)
    print s.fractionToDecimal(500, 10)
    print s.fractionToDecimal(22, 7)
    print s.fractionToDecimal(1, 99)
    print s.fractionToDecimal(1, 5)
    print s.fractionToDecimal(2, -9)
    print s.fractionToDecimal(-2, 9)
    print s.fractionToDecimal(2, 9)