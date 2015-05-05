# coding=utf8

__author__ = 'smilezjw'

class TwoSum:
    def __init__(self):
        # 初始化hash表
        self.hashtable = dict()

    def add(self, number):
        self.hashtable[number] = self.hashtable.get(number, 0) + 1

    def find(self, value):
        for i in self.hashtable.keys():
            j = value - i
            # 如果两个数字相同，则判断该数字是否出现至少两次
            # 如果两个不同数字，则判断j是否在hash表中
            if i == j and self.hashtable.get(i) > 1 or i !=j and self.hashtable.get(j, 0) > 0:
                return True
        return False

##################################################################################
# 这道题要求设计数据结构，能够支持添加数据以及查找两数之和等于目标数。
# 初始化hash表，键为添加进去的数字，值为该数字出现的次数。其实查找的操作和P1的思路
# 是一样的，只是还要考虑到这里两个相同的数字之和等于目标数也可以，只要该数字出现了
# 一次以上。
#