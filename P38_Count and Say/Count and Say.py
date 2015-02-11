# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def countAndSay(self, n):  # 还以为规则就这3条呢= =
    #     s = '1'
    #     for count in xrange(n):
    #         res = ''
    #         i = 0
    #         while i < len(s):
    #             if i < len(s) - 1 and s[i] + s[i+1] == '11':
    #                 res += '21'
    #                 i += 1
    #             elif s[i] == '1':
    #                 res += '11'
    #             elif s[i] == '2':
    #                 res += '12'
    #             i += 1
    #         s = res
    #     return s

    def countAndSay(self, n):
        s = '1'
        for i in xrange(1, n):
            res = ''   # 第i项数字序列
            prev = ''  # 记录前一个数字
            count = 0  # 记录数字的个数
            for number in s:
                if number != prev and prev != '': # 遇到不相同的数字，开始转换
                    res += str(count) + prev      # 其实就是这个数字有几个，连着这个数字
                    count = 1                     # 开始对number计数
                else:
                    count += 1
                prev = number                     # 记录前一个数字
            res += str(count) + number            # 得到第i个数字序列的字符串
            s = res
        return s

if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(1)  # 1 --> 1
    print s.countAndSay(2)  # 2 --> 11
    print s.countAndSay(3)  # 3 --> 21   4 --> 1211  5 --> 111221
    print s.countAndSay(6)  # 6 --> 312211

###############################################################################################
# 一开始我以为只有3条规则，原来就是有多少个相邻的相同数字，然后拼接这个数字，最终得到结果的
# 字符串。
#