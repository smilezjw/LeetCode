# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def isOneEditDistance(self, s, t):
        sLen = len(s)
        tLen = len(t)
        # 如果s为空，则t只能是增加了一个字符
        if not s:
            return tLen == 1
        # 如果t为空，则s只能是增加了一个字符
        elif not t:
            return sLen == 1
        # 如果s和t长度相同，则计算s和t有多少个不同的字符，
        # 如果仅有一个不同字符则返回True，否则返回False
        if sLen == tLen:
            count = 0
            for i in xrange(sLen):
                if s[i] != t[i]:
                    count += 1
            return count == 1
        # 如果s和t长度差1，则首先判断哪个字符串更长
        elif abs(sLen - tLen) == 1:
            if sLen > tLen:
                ss = t
                ll = s
            else:
                ss = s
                ll = t
            i = j = count = 0
            # 判断s和t中有多少个不同字符
            # 如果没有不同字符，例如abcd和abc，此时j指向较长的字符串的最后一位字符
            # 如果有一个不同字符，则符合条件
            while i < len(ss) and j < len(ll):
                if ss[i] != ll[j]:
                    count += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            return count == 1 or count == 0 and j == (len(ll)-1)
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print s.isOneEditDistance('', '')
    print s.isOneEditDistance('', 'a')
    print s.isOneEditDistance('', 'ab')
    print s.isOneEditDistance('a', '')
    print s.isOneEditDistance('ab', '')
    print s.isOneEditDistance('abcdefg', 'abcdefg')
    print s.isOneEditDistance('abcdefg', 'abcdef')
    print s.isOneEditDistance('abcdef', 'abcdefg')
    print s.isOneEditDistance('abcdefg', 'accdefg')
    print s.isOneEditDistance('abcdefg', 'abccef')

######################################################################################
# 这道题和P72类似，主要考虑add和delete都使得s和t长度相差1，而replace使得s和t长度相同。
#