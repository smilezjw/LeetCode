# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def reverseBits(self, n):
        res = 0
        bits = []
        for i in xrange(32):
            bits.append(n & 1)
            n >>= 1
        for i in xrange(32):
            res += bits[i] * (2 ** (31 - i))
        return res

    # 这种写法果然比较简洁
    def reverseBitsII(self, n):
        res = 0
        for i in xrange(32):
            res <<= 1     # res左移乘以2
            # n&1得出最低位是否为1，然后和res进行或操作
            # 0或者1和1位与还是其本身，0或者1和0位或还是其本身
            res |= n & 1
            n >>= 1       # n右移除以2
        return res

if __name__ == '__main__':
    s = Solution()
    print s.reverseBits(1)
    print s.reverseBits(0)
    print s.reverseBits(43261596)
    print s.reverseBits(3)
    print s.reverseBits(11)
    print s.reverseBits(2**31-1)
    print s.reverseBitsII(1)

######################################################################################
# 这道题比较简单，重点是能够写出简洁的代码，重点考察的还是位操作。
#