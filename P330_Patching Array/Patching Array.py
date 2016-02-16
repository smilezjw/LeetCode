# coding=utf8

class Solution(object):
    def minPatches(self, nums, n):
        # miss表示[0,miss)中已经能够覆盖所有数字，左闭右开
        miss = 1
        i = 0
        res = 0
        size = len(nums)
        while miss <= n:
            # 如果nums[i] <= miss， 则覆盖的范围增加到[0,miss+nums[i])
            if i < size and nums[i] <= miss:
                miss += nums[i]
                i += 1
            # 如果nums[i] > miss，则[0,miss)到nums之间有gap，先加上miss这个数再判断，覆盖的范围增加到[0, miss+miss)
            else:
                miss += miss
                res += 1
        return res


if __name__ == '__main__':
    nums0 = [1, 3]
    s = Solution()
    print s.minPatches(nums0, 6)

    nums1 = [1, 5, 10]
    print s.minPatches(nums1, 20)

###################################################################################
# https://leetcode.com/discuss/82822/solution-explanation
#
