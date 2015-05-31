# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        length = len(nums)
        if length == 0 or k == 0:
            return False
        if k > length:
            k = length
        for i in xrange(length-k+1):
            for j in xrange(i+1, i+k):
                if nums[i] == nums[j]:
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    nums0 = []
    nums1 = [1]
    nums2 = [1, 2, 3, 1, 6, 8]
    # print s.containsNearbyDuplicate(nums0, 3)
    # print s.containsNearbyDuplicate(nums1, 1)
    # print s.containsNearbyDuplicate(nums2, 0)
    print s.containsNearbyDuplicate(nums2, 10)
    print s.containsNearbyDuplicate(nums2, 5)

    nums3 = [99, 99]
    print s.containsNearbyDuplicate(nums3, 2)