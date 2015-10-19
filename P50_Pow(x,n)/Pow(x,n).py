# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def pow(self, x, n):  # 对于2**31-1次幂会超时
    #     if n == 0:
    #         return 1
    #     i = 1
    #     res = 1
    #     while i < n:
    #         if i == 1:
    #             res = x
    #         else:
    #             res *= res
    #         i = i << 1
    #     i = i >> 1
    #     for j in xrange(i+1, n):
    #         res *= x
    #     res *= x
    #     return res

    def pow(self, x, n):  # 采用递归，类似于二分的思路，多么brilliant的做法
        if n == 0:
            return 1.0
        elif x == 0 and n < 0:
            return 1.0
        elif n < 0:  # 这里还要考虑n为负数的时候,转化为求1/x的-n次幂
            return self.pow(1/x, -n)
        elif n % 2:  # n为奇数，x的n次幂 = x的n/2次幂 * x的n/2次幂 * x
            return self.pow(x*x, n/2) * x
        else:        # n为偶数，x的n次幂 = x的n/2次幂 * x的n/2次幂
            return self.pow(x*x, n/2)

if __name__ == '__main__':
    s = Solution()
    print s.pow(3.0, -10)
    print s.pow(3.0, 10)
    print s.pow(0.00001, 2147483647)
    print s.pow(0, 0)
    print s.pow(0, 5)
    print s.pow(0, -5)

##########################################################################################
# 自己写的果然会超时= = 采用递归的方法，类似于二分法的思路，判断n为奇数还是偶数，多么聪明
# 的方法。
#