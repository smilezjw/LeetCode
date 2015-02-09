# coding=utf8

__author__ = 'smilezjw'


def divide(dividend, divisor):
    MAX_INT = 2 ** 31 - 1
    if divisor == 0:
        return MAX_INT  # 除数为0溢出
    if (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0):
        flag = 1         # 记录商的正负号
    else:
        flag = -1
    dividend = abs(dividend) # 用绝对值进行计算
    divisor = abs(divisor)
    count = 1                # 2的幂次，和除数同时左移或右移
    quotient = 0             # 商为2的幂次之和
    temp = divisor
    while dividend >= temp:  # 首先左移，每次左移都是乘2，找到最大的幂次
        temp = temp << 1
        count = count << 1
    while dividend >= divisor:
        while temp > dividend:
            temp = temp >> 1   # 如果除数大于被除数，则右移除以2
            count = count >> 1 # 同时2的幂次也要右移除以2
        quotient += count
        dividend -= temp
    res = flag * quotient
    if res >= MAX_INT:      # 判断溢出情况
        return MAX_INT
    else:
        return res

if __name__ == '__main__':
    print divide(-10, 5)
    print divide(1, -1)
    print divide(11, 0)
    print divide(-3, 2)
    print divide(-2147483648, -1)

###############################################################################################
# 首先看到这道题第一反应是被除数不断减去除数，直至被除数小于除数为止，记录减去了多少个除数即可
# 得到商。但是这样的做法遇到(2 ** 31 - 1) / 1 就非常非常慢，不能被accept。
# 这道题可以用二分查找的思路，用被除数减去除数的2的幂次，例如：
# 13 / 3 = 3 * 2^2 + 1，商为2^2 = 4;  47 / 7 = 7 * 2^2 + 7 * 2^1 + 5,商为2^2 + 2^1 = 5
# 所以通过位运算，左移表示乘以2，右移表示除以2，将除数不断左移直至大于被除数，然后开始右移，
# 被除数减去除数，同时有一个变量记录2的幂次，直至被除数小于除数。