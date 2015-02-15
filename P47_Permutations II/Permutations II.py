# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def permuteUnique(self, num):
        if len(num) <= 1:
            return [num]
        num.sort()    # 先对列表进行排序
        res = []
        prev = None   # 记录前一个数字
        for i in xrange(len(num)):
            if num[i] == prev:  # 如果连续两个重复数字的话，就会出现重复解，因此需要剪枝
                continue
            prev = num[i]
            for j in self.permuteUnique(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique([1, 1, 2])

############################################################################################
# 这道题如果直接在46题的基础上求解然后判断res[]列表中是否重复，重复则丢弃重复解，这种思路
# 会超时。因此，需要在求解之前就需要剪枝，先对列表进行排序；然后判断连续两个数字是否相同，
# 如果相同则会出现重复解，因此对连续重复的数字进行剪枝。
#
