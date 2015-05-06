# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 一开始想到这种方法，不能处理负数啊
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            count += n & 1  # n和1做位与操作，计算最低位的1的个数， 还可以n%2也是取得最低位1的个数
            n >>= 1         # n向右移一位相当于n /= 2
        return count

    # 这种方法需要循环n的二进制位数次
    def hammingWeight_II(self, n):
        count = 0
        flag = 1
        while flag:
            if (flag & n):
                count += 1
            flag <<= 1
        return count

    # 把一个整数减去1，再和原来的整数做位与运算，会把该整数最右边一个1变成0。
    # 那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作。
    def hammingWeight_III(self, n):
        count = 0
        while n:
            count += 1
            n &= (n-1)
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