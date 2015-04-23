# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 时间复杂度为O(n)，空间复杂度为O(n)
    # 这种方法重新构造数组nums，不满足条件‘原地旋转’
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

    # 完美洗牌算法，时间复杂度为O(n)，空间复杂度为O(1)
    # [1, 2, 3, 4, 5, 6, 7] => [5, 6, 7, 1, 2, 3, 4]
    # 位置变化情况为： 1 -> 4 -> 7 -> 3 -> 6 -> 2 -> 5 -> 1
    # 也会出现死循环的情况： [1, 2, 3, 4, 5, 6] => [4, 5, 6, 1, 2, 3]
    # 位置变化为： 1 -> 4 -> 1, 2 -> 5 -> 2,  3 -> 6 -> 3
    def rotateII(self, nums, k):
        length = len(nums)
        k %= length
        idx = 0         # 记录位置
        distance = 0    # 记录是否又回到第0个元素，避免死循环
        curr = nums[0]  # 当前需要重新放置位置的元素
        for i in xrange(length):
            next = (idx + k) % length  # 找到当前元素需要放置的位置
            temp = nums[next]          # 用temp记录需要放置的位置的元素
            nums[next] = curr          # 将当前元素放置到新的位置上
            idx = next
            curr = temp                # 然后当前元素变为了原来该位置上的元素
            distance = (distance + k) % length  # 这是避免出现死循环
            if distance == 0:
                idx = (idx + 1) % length
                curr = nums[idx]
        return nums

    # 以length-k为界，分别对数组左右两边进行逆置，然后对整个数组逆置
    # [1, 2, 3, 4, 5, 6, 7] => [4, 3, 2, 1, 7, 6, 5] => [5, 6, 7, 1, 2, 3, 4]
    # 时间复杂度为O(n),空间复杂度为O(1)
    def rotateIII(self, nums, k):
        length = len(nums)
        k %= length
        self.reverse(nums, 0, length-1-k)
        self.reverse(nums, length-k, length-1)
        self.reverse(nums, 0, length-1)
        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    nums2 = [1, 2]
    nums3 = [1, 2, 3, 4, 5, 6]
    # print s.rotate(nums, 3)
    # print s.rotate(nums2, 3)
    # print s.rotateII(nums, 3)
    # print s.rotateII(nums3, 3)
    print s.rotateIII(nums, 3)

#######################################################################################
# 这道题一共采用3种做法：
# 1.第一种做法是最开始想到的，时间复杂度和空间复杂度都为O(n)，开辟了一个新的数组。
# 2.第二种做法实现比较难想到，用的是完美洗牌算法，时间复杂度为O(n)，空间复杂度为O(1)。
# 3.第三种做法也比较好理解，分别对length-k前后两部分数组进行逆置，然后对整个数组进行
# 逆置，时间复杂度为O(n)，空间复杂度为O(1)。
#