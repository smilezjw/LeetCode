# coding=utf8

__author__ = 'smilezjw'


def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = 0
    for i in xrange(1, len(s)):
        if roman[s[i - 1]] < roman[s[i]]:
            values -= roman[s[i-1]]
        else:
            values += roman[s[i-1]]
    values += roman[s[-1]]
    return values

if  __name__ == '__main__':
    print romanToInt('I')
    print romanToInt('CXCIX')

##############################################################################################
# 这道题比上一道integer to roman简单，因为这道题只要再7个罗马字符内考虑左减右加的规律就可以了。
# 从字符串的第0个字符开始考虑，如果该字符表示的数字小于右边字符，则做减法；否则做加法。
#
