# coding=utf8

__author__ = 'smilezjw'


class Solution(object):
    def singleNumber(self, nums):
        # 0和一个数字异或结果为该数字本身
        # 异或同0异1
        # 所有数字都异或，结果为两个single number的异或结果
        xor = reduce(lambda x, y: x ^ y, nums)
        # 由于两个single numbers是不相同的，因此异或结果肯定至少有一位为1
        # 通过和其自身相反数进行位与操作，取得最低位
        lowbit = xor & -xor
        a = b = 0
        # 根据最低位找到两个single numbers
        for num in nums:
            if num & lowbit:
                a ^= num
            else:
                b ^= num
        return [a, b]
