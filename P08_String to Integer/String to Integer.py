# coding=utf8

__author__ = 'smilezjw'


def atoi(str):
    str = str.strip(' ')
    positive = 1
    number = 0
    count = 0
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    for i in str:
        if i == '-':
            positive = -1
            count += 1
        elif i == '+':
            positive = 1
            count += 1
        elif i >= '0' and i <= '9':
            number = number * 10 + int(i)
        else:
            break
    if count >= 2:
        return 0
    elif positive * number > INT_MAX:  #判断正数上溢
        return INT_MAX
    elif positive * number < INT_MIN:  #判断负数下溢
        return INT_MIN
    else:
        return positive * number

if __name__ == '__main__':
    print atoi('   123 ')
    print atoi('  -1 23 ')
    print atoi('+-1')
    print atoi('-12a32')  ##遇到非数字的字符，后面的字符全都忽略

#################################################################################################
# 这道题有点无语，主要还是看出题者的意图，没有明确表示谁知道他是想要哪些条件符合哪些条件不符合= =
# 主要还是看判断字符和溢出情况吧，这道题和第7题都考虑了整数溢出的情况。
#