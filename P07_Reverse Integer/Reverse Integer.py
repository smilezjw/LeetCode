# coding=utf8

__author__ = 'smilezjw'


def reverse(x):
    positive = 1
    y = 0
    if x < 0:
        positive = -1
        x = abs(x)
    while x >= 10:
        y = y * 10 + x % 10
        x = x / 10
    x = x + y * 10
    #假设输入是32-bit 整数，如果输入为1000000003，则输出会溢出，因此出现溢出则输出为0
    # 注意有符号位的32-bit integer应该表示为2^31 - 1， 如果是无符号位的32-bit integer应该表示为2^32 - 1
    if x >= 2 ** 31 - 1:
        return 0
    else:
        return positive * x


if __name__ == '__main__':
    print reverse(123)
    print reverse(-123)
    print reverse(0)
    print reverse(100)
    print reverse(90100)
    print reverse(1000000003)

########################################################################################
# 这道题整体比较简单，主要是需要考虑特殊情况，如负数、100等，
# 这道题我卡顿在如何表示32-bit integer,注意有符号位的32-bit integer应该表示为2^31 - 1，
# 如果是无符号位的32-bit integer应该表示为2^32 - 1。
#