# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def containsDuplicate(self, nums):
        if not nums:
            return False
        hashTable = {}
        for i in xrange(len(nums)):
            hashTable[nums[i]] = hashTable.get(nums[i], 0) + 1
            if hashTable[nums[i]] > 1:
                return True
        return False

################################################################################
# 这道题主要考hash table。
#