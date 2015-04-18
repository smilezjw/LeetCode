# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # O(n)线性遍历列表
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        for i in xrange(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1


    # 分治法
    def search(self, nums, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return start if nums[start] > nums[end] else end
        mid = (start + end) / 2
        if nums[mid] < nums[mid-1]:
            return self.search(nums, start, mid-1)
        if nums[mid] < nums[mid+1]:
            return self.search(nums, mid+1, end)
        return mid

    def findPeakElement_Binary(self, nums):
        return self.search(nums, 0, len(nums)-1)


if __name__ == '__main__':
    s = Solution()
    print s.findPeakElement([1, 2, 3, 1])
    print s.findPeakElement([1, 2])
    print s.findPeakElement([3, 2, 1])
    print s.findPeakElement_Binary([1, 2, 3, 1])
    print s.findPeakElement_Binary([3, 2, 1])

###################################################################################################
# 这道题可以用两种解法求解：
# 1.线性遍历数组，最容易想到，时间复杂度为O(n)。
# 2.分治法，时间复杂度为O(logn)：首先去列表中间的元素nums[mid]，如果该元素大于左右相邻元素，则该元素
# 就是peak element；如果nums[mid-1] > nums[mid]，则向左递归搜索，如果nums[mid-1] > nums[mid-2]，则
# nums[mid-2]就是peak element；否则继续比较nums[mid-2]和nums[mid-3]大小；直到nums[1]和nums[0],其中必
# 然有peak element。同样的，如果nums[mid+1] > nums[mid]，向右递归搜索。只需要找到一个peak element即可。
#