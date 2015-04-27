# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def countPrimes_Sieve(self, n):
        if n < 2:
            return 0
        hashtable = [True] * n
        hashtable[0] = False
        hashtable[1] = False
        i = 2    # 2是第一个素数
        while i * i < n:  # 从i的平方开始枚举
            if hashtable[i]:
                j = i
                while i * j < n:  # 大于等于i的平方小于n的数中，枚举i的倍数
                    hashtable[i * j] = False
                    j += 1
            i += 1
        return sum(hashtable)  # 这里sum是将所有为True的个数进行计数

if __name__ == '__main__':
    s = Solution()
    print s.countPrimes_Sieve(12)
    print s.countPrimes_Sieve(49979)

####################################################################################
# 这是一道数学题啊= = 使用Sieve of Eratosthenes的方法计算所有小于等于n的素数个数：
# step1.创建一个hash表记录从2到n,[2, 3, 4, ..., n]是否为素数的状态，初始时都设为True；
# step2.初始时让p等于2， 2是第一个素数；
# step3.从p开始，枚举p的所有小于n的倍数，(2p, 3p, 4p, ...)，在hash表中将这些倍数的
# 状态设置为False；
# step4.找到大于p小于n的后面第一个数，如果没有这样的数则算法停止；否则让p等于该数，
# 重复上述step3。
# 当算法结束时，哈希表中所有为True状态的数字（也就是索引）都是素数。
# 如果仅仅是这样，Leetcode还是会超时，仍然有点改进的地方是：在step3时从大于等于p的
# 平方的倍数开始枚举，因为比p的平方更小的倍数之前已经判断过了。例如在判断5的倍数时，
# 其中10也是2的倍数，已经判断过了，因此直接从25开始设置状态。
#