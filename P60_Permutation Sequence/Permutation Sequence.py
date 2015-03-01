# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def getPermutation(self, n, k):
        res = ''
        k -= 1  # 注意首先要将k减去1，因为从0开始计数
        fac = 1
        for i in xrange(1, n):
            fac *= i
        num = [i for i in xrange(1, n+1)]
        for i in xrange(n-1, -1, -1):
            curr = num[k / fac]
            res += str(curr)
            num.remove(curr)
            if i != 0:
                k %= fac
                fac /= i
        return res

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(6, 400)

#########################################################################################
# 参考人家的思路：假设n=6, k=400（k首先减1，因为直接从1开始计数的而不是从0开始计数）
# 先计算第一位，如果第一位为6，最少也是第5！* 5 + 1 = 601个排列，因为前面1/2/3/4/5各有5！
# 个排列，此时排列为612345; 由于601 > 399，计算 k / 5! = 3，也就是说前面有3个5！的排列，
# 则第一位应该取到4；下面不能再取到4，因此列表中将4删除。此时k = k % 5! = 39;
# 然后计算第二位，此时待选数字为1/2/3/5/6，39 / 4! = 1, 也就是说前面有1个4！的排列，则第二
# 位应该取2；然后列表中将2删除。此时k = k % 4! = 15;
# 然后计算第三位，此时待选数字1/3/5/6, 15 / 3! = 2, 也就是说前面有2个3！的排列，则第三位应
# 该取5；然后列表中将5删除。 此时k = k % 3! = 3;
# 然后计算第四位，此时待选数字1/3/6， 3 / 2！ = 1, 则第四位应该取3；k = k % 2! = 1;
# 然后计算第五位，此时待选数字1/6， 1 / 1! = 1, 则第五位应该取6; k = k % 1! = 0;
# 最后计算最后一位，此时只能选1了，0 / 1! = 0。
# 完成计算。