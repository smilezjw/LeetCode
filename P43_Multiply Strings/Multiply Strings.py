# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def multiply_1(self, num1, num2):
        res = 0
        for i in reversed(xrange(len(num2))):
            for j in reversed(xrange(len(num1))):
                res += (int(num2[i]) * 10 ** (len(num2) - i - 1)) * (int(num1[j]) * 10 ** (len(num1) - j - 1))
        return res

    def multiplyDirectly(self, num1, num2):
        return str(int(num1) * int(num2))

    def multiply(self, num1, num2):  # 大数乘法
        num1 = num1[::-1]  # 反转字符串，用分片来做
        num2 = num2[::-1]
        arr = [0 for i in xrange(len(num1) + len(num2))]  # 乘数最多位数为len(num1) + len(num2)位
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])  # 最精彩的在这一步，用位运算来做
        res = []
        for i in xrange(len(arr)):
            digit = arr[i] % 10  # 每一位上保留的数字
            carry = arr[i] / 10  # 每一位的进位
            if i < len(arr) - 1:
                arr[i+1] += carry  # 进位操作
            res.insert(0, str(digit))
        while res[0] == '0' and len(res) > 1:  # 把初始值的0给删除掉
            res.remove('0')
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    #print s.multiply_1('12', '12')
    #print s.multiplyDirectly('12', '12')
    print s.multiply('12', '12')
    print s.multiply('16', '16')

###############################################################################################
# 这道题想要考大数乘法，用位运算来做还是很精彩的。
# 先将两个字符串反转过来，用分片来做；然后按位进行相乘，相乘的结果直接保留到列表中，先不要进位；
# 然后对列表中的数字对10求余则是该位保留的结果，除以10则是该位的进位，将进位加到下一位中继续操
# 作，最后注意将初始值0删除掉。
#