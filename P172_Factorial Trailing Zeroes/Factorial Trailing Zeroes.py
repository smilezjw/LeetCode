# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 递归
    def trailingZeroes_Recurrsion(self, n):
        if n < 5:
            return 0
        else:
            return n / 5 + self.trailingZeroes_Recurrsion(n / 5)

    # while循环非递归
    # 考虑n!的质数因子，后缀0总是由质因子2和质因子5相乘得来的，而2的个数总是大于等于5的个数，
    # 因此只要计算5的个数即可。
    # 计算n!中5的个数，floor(n/5)，例如6！中有1个5,11！中有2个5，还要注意如25中不止一个5，
    # 例如26！有6个5分别为5，10,15，20分别1个5和25中的两个5。
    # 因此可以归纳得出计算后缀0的公式为n/5 + n/25 + n/125 + ...
    def trailingZeroes(self, n):
        x = 5
        res = 0
        while n >= x:  # 直到n等于0为止
            res += n / x
            x *= 5
        return res

if __name__ == '__main__':
    s = Solution()
    print s.trailingZeroes(25)
    print s.trailingZeroes_Recurrsion(26)

###############################################################################################
# 如果直接计算n的阶乘，那遇到稍微大点数字计算阶乘就会溢出了。
# 这里归纳得出计算后缀0个数的公式。
#