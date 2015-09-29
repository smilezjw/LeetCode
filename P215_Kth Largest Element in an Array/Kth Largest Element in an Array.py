# coding=utf8

__author__ = 'smilezjw'

import random


class Solution:
    def findKthLargest_Solution1(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for n in nums:
            if n > pivot:
                nums1.append(n)
            elif n < pivot:
                nums2.append(n)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot

    def findKthLargest_Solution2(self, nums, k):
        return sorted(nums, reverse=True)[k-1]
