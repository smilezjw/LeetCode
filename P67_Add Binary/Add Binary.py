# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def addBinary(self, a, b):
        len_a = len(a) - 1
        len_b = len(b) - 1
        res = ''
        carry = 0  # 进位标志
        while len_a >= 0 and len_b >= 0:
            temp = int(a[len_a]) + int(b[len_b]) + carry
            carry = temp / 2
            temp %= 2
            res = str(temp) + res  # 这样从右往左记录， res += str(temp)从左往右记录
            len_a -= 1
            len_b -= 1
        while len_a >= 0:
            temp = int(a[len_a]) + carry
            carry = temp / 2
            temp %= 2
            res = str(temp) + res
            len_a -= 1
        while len_b >= 0:
            temp = int(b[len_b]) + carry
            carry = temp / 2
            temp %= 2
            res = str(temp) + res
            len_b -= 1
        if carry == 1:  # 千万别忘了最后一位是否进位
            res = '1' + res
        return res

if __name__ == '__main__':
    s = Solution()
    print s.addBinary('1111','100')

##########################################################################################
# 这道题是细节题，在字符串处理的过程和最后一位是否需要进位的判断都需要注意。和66题都是
# 差不多类型的。
#