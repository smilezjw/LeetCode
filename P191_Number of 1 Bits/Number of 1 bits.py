# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            count += n & 1  # n和1做位与操作，计算最低位的1的个数， 还可以n%2也是取得最低位1的个数
            n >>= 1         # n向右移一位相当于n /= 2
        return count

if __name__ == '__main__':
    s = Solution()
    print s.hammingWeight(0)
    print s.hammingWeight(11)
    print s.hammingWeight(2**31-1)

######################################################################################
# 这道题比较简单，方法也很多，但思路是一致的，对n取得最低位1的个数，然后n右移相当于
# 除以2。这里对n取最低位1的个数可以和1位与操作，可以模2取余数等。
#