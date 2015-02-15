# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def permute(self, num):
        if len(num) <= 1:
            return [num]
        res = []
        for i in xrange(len(num)):
            for j in self.permute(num[:i] + num[i+1:]):  # 递归
                res.append([num[i]] + j)  # 列表相加相当于append的作用
        return res

if __name__ == '__main__':
    s = Solution()
    print s.permute([1, 2, 3])

############################################################################################
# 对于这种递归的做法真的不熟悉，需要跟着调试一步一步走。
#