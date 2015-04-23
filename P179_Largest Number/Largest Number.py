# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def largestNumber(self, nums):
        # 首先将数字转换为字符串，比较相邻两个字符串，
        # 如果str(a) + str(b) > str(b) + str(a)则a排在b的前面，否则b排在a的前面
        # 时间复杂度为O(nlogn)
        nums = sorted([str(n) for n in nums], cmp=self.compare)
        res = ''.join(nums).lstrip('0')
        return res or '0'  # 避免只有一个0的情况下返回空

    def compare(self, a, b):
        return [1, -1][(a+b) > (b+a)]

if __name__ == '__main__':
    s = Solution()
    print s.largestNumber([0])
    print s.largestNumber([0, 00])
    print s.largestNumber([1, 3, 30, 34, 5, 9])

#######################################################################################
# 这道题使用python的内置排序，自定义排序规则，比较相邻两个由整数转化的字符串，
# 如果str(a) + str(b) > str(b) + str(a)则a排在b的前面，否则b排在a的前面。
# 时间复杂度为O(nlogn)。需要注意一些特殊情况，如[0], [0, 0]等。
#