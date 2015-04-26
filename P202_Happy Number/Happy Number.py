# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def isHappy(self, n):
        hashtable = []
        while n != 1 and n not in hashtable:
            hashtable.append(n)
            temp = 0
            while n != 0:
                # 计算每一位数字的平方和，从个位数开始计算
                temp += (n % 10) ** 2
                n = (n - n % 10) / 10
            n = temp
        return n == 1


if __name__ == '__main__':
    s = Solution()
    print s.isHappy(2)
    print s.isHappy(19)

#####################################################################################
# 采用hash表，如果是happy number则总能计算得到平方和为1；否则不是happy number则会在
# hash表中重复出现。
#