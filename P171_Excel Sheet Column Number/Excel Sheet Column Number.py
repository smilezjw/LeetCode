# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 将26进制转化为10进制
    def titleToNumber(self, s):
        res = 0
        length = len(s)
        for i in xrange(length):
            res += (ord(s[length - 1 - i]) - 65 + 1) * (26 ** i)  # AB = 1 * 26 ^ 1 + 2 * 26 ^ 0 = 28
        return res

if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber('A')
    print s.titleToNumber('AA')
    print s.titleToNumber('ABZ')

#####################################################################################################
# 这道题和P168思路是反过来的，这道题是将26进制转化为20进制。注意这里的26进制是从1-26，而不是0-25，所以
# 26进制都要加1的。
# 这里用ord()将字符转换为ASCII码，A-Z的ACII范围为65-90。
#