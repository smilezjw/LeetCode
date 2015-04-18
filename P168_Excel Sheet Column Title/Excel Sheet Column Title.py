# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 进制转换，10进制转化为26进制
    def convertToTitle(self, n):
        # chr(i) return a string of one character whose ASCII code is the integer i.
        table = [chr(i) for i in xrange(65, 91)]
        res = ''
        while n > 0:
            # 除以26取余数
            remainder = n % 26
            res = table[remainder-1] + res
            n /= 26
            # 由于这里的26进制从1-26，并不是0-25（都多了1），所以当余数为0时要特殊处理
            # 例如26除以26的余数为0，这时候要(26-1)%26
            if remainder == 0:
                n -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print s.convertToTitle(52)
    print s.convertToTitle(26)
    print s.convertToTitle(2)
    print s.convertToTitle(28)
    print s.convertToTitle(704)

###################################################################################################
# 这道题其实是进制转换的题目，将10进制转换为26进制，但是需要注意的是这里的26进制是从1-26，并不是
# 0-25（多了1）,因此需要将给出的10进制数减1然后再除以26取余数。
# 这里学会用chr()函数返回0-255ASCII码对应的字符。
#