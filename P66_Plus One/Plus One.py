# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def plusOne(self, digits):
        digits[-1] += 1
        if digits[-1] >= 10:  # 加1，判断是否需要进位，不进位的话直接返回就可以了
            digits[-1] -= 10
            carry = 1  # 进位标志
            for i in xrange(len(digits)-2, -1, -1):
                digits[i] += carry      # 加上进位
                carry = digits[i] / 10  # 判断是否需要再进位
                digits[i] %= 10
            if carry == 1:              # 如果最高位需要进位，则在列表第0个位置插入1
                digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    s = Solution()
    digits = [9, 9]
    print s.plusOne(digits)

#########################################################################################
# 和67题差不多，都是加法利用列表来判断是否进位，逐位处理。
#