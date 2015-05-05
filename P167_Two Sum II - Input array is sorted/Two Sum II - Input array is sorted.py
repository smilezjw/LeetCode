# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 两个指针
    def twoSum(self, num, target):
        left = 0
        end = len(num) - 1
        while left < end:
            if num[left] + num[end] == target:
                return (left, end)
            elif num[left] + num[end] < target:
                left += 1
            else:
                end -= 1
        return None

if __name__ == '__main__':
    s = Solution()
    num0 = [2, 7, 11, 15]
    print s.twoSum(num0, 9)

    num1 = []
    print s.twoSum(num1, 1)

    num2 = [2, 7, 11, 15]
    print s.twoSum(num2, 10)

#################################################################################
# 付费题目所以没有Online Judge，题目意思是给定数组已经按升序排列，给定一个目标找
# 到两个相加等于该目标的数字在数组中的下标。
# 用两个指针分别指向数组第0个位置和最后一个位置，然后判断两个数之和与目标数字的大
# 小关系，如果两数之和大于目标数，则右指针向左移；如果两数之和小于目标数，则左指针
# 向右移，直到两个指针相遇或者找到符合要求的两个数字为止。
#