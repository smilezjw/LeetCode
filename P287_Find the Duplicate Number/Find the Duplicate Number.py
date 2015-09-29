# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def findDuplicate(self, nums):
        low = 1
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            cnt = sum(x <= mid for x in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low

if __name__ == '__main__':
    s = Solution()
    # print s.findDuplicate([1,1,2])
    # print s.findDuplicate([1,1,1])
    print s.findDuplicate([1,2,2,3,4,5])


##########################################################################################
# 不允许修改数组意味着禁止排序，常数空间复杂度意味着不能使用dict等数据结构。小于O(n^2)的
# 运行时间可以联想到用二分查找将其中的一个n减少到logn。
# 鸽巢原理，给定n+1个数，范围在[1,n]之间，其中一定存在至少一个数出现至少两次。
# 遍历数组，若数组中不大于n/2的数字超过n/2个，则可以确定重复的数字在[1, n/2]之间；否则重复
# 的数字在（n/2， n]之间。
#
