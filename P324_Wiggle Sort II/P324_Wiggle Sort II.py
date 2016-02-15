# coding=utf8

class Solution(object):
    def wiggleSort(self, nums):
        temp  =sorted(nums)
        length = len(nums)
        for i in range(1, length, 2) + range(0, length, 2):
            nums[i] = temp.pop()
        return nums

        # 这种做法会导致[1, 3, 2, 2, 3, 1]中两个2放在一起
        # temp = sorted(nums)
        # i = 0
        # j = len(nums)-1
        # c = 0
        # while i < j:
        #     nums[c] = temp[i]
        #     nums[c+1] = temp[j]
        #     i += 1
        #     j -= 1
        #     c += 2
        # if len(nums) % 2 == 1:
        #     nums[-1] = temp[i]
        # return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 2, 2, 3, 1]
    print s.wiggleSort(nums)

