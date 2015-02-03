# coding=utf8

__author__ = 'smilezjw'


def longestPalindrome(s):
    if len(s) == 1:
        return s
    p = s[0]
    # 遍历中心点，以中心点向两侧取出回文字符串
    for i in range(1, len(s)):
        # 如果长度是奇数回文字符串，如‘abcba'
        m = palindrome(s, i, i)
        # 如果长度是偶数回文字符串，如‘abba’
        n = palindrome(s, i-1, i)
        mlen = len(m)
        nlen = len(n)
        plen = len(p)
        if mlen > len(p) and mlen > nlen:
            p = m
        if nlen > len(p) and nlen > mlen:
            p = n
    return p

# 从中间位置开始判断是否是回文字符串
def palindrome(s, begin, end):
    while (begin >= 0)and (end < len(s)) and s[begin] == s[end]:
        begin -= 1
        end += 1
    return s[begin + 1: end]


if __name__ == '__main__':
    print longestPalindrome('abb')
    print longestPalindrome('eabcbaxabcdedcbaf')
    print longestPalindrome('ccc')
    print longestPalindrome('ccd')

###############################################################################
# 遍历中心点，对每一个中心点都向两侧扩散判断是否为回文字符串，需要考虑两种情况：
# 1.奇数长度回文字符串
# 2.偶数长度回文字符串
# 时间复杂度为O(n^2).
#