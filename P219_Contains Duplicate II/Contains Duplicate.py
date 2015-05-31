# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # 使用hashmap保存数组中每个元素的下标
        numDict = {}
        for i in xrange(len(nums)):
            idx = numDict.get(nums[i])
            if idx >= 0 and i - idx <= k:
                return True
            numDict[nums[i]] = i
        return False

if __name__ == '__main__':
    s = Solution()
    nums0 = []
    nums1 = [1]
    nums2 = [1, 2, 3, 1, 6, 8]
    print s.containsNearbyDuplicate(nums0, 3)
    print s.containsNearbyDuplicate(nums1, 1)
    print s.containsNearbyDuplicate(nums2, 0)
    print s.containsNearbyDuplicate(nums2, 10)
    print s.containsNearbyDuplicate(nums2, 5)

    nums3 = [99, 99]
    print s.containsNearbyDuplicate(nums3, 2)

    nums4 = [-1, -1]
    print s.containsNearbyDuplicate(nums4, 1)

##########################################################################################
# 这道题与P217题类似，也是采用hash table的思路，记录数组中每个元素的下标，然后判断是否存在
# 两个相同的元素并且下标只差小于等于k。
#