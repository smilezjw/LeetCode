# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def findMin(self, num):
        if len(num) == 1:
            return num[0]
        left = 0
        right = len(num) - 1
        while left <= right:
            mid = (left + right) / 2
            if num[left] <= num[mid] <= num[right]:  # 如果是递增序列，则num[left]是最小的
                return num[left]
            elif num[right] <= num[mid] <= num[left]:  # 如果是递减序列，则num[right]是最小的
                return num[right]
            elif num[mid] > num[left]:  # 旋转的部分在右边
                left = mid
            elif num[mid] < num[right]:  # 旋转的部分在左边
                right = mid
        return -1

    def findMin_Second(self, num):
        left = 0
        right = len(num) - 1
        while left < right and num[left] > num[right]:  # 旋转的序列满足num[left] > num[right
            mid = (left + right) / 2
            if num[mid] < num[right]:  # 旋转的部分在左边
                right = mid
            else:                      # 旋转的部分在右边
                left = mid + 1
        return num[left]

if __name__ == '__main__':
    s = Solution()
    num = [4, 5, 6, 7, 0, 1, 2]
    num2 = [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
    num3 = [7, 8, 9, 0, 1, 2, 3, 4, 5]
    print s.findMin_Second(num2)

##########################################################################################
# 这道题采用二叉查找来求解，我采用的思路是通过判断num[left] <= num[mid] <= num[right]或者
# num[right] >= num[mid] >= num[left]， 判断是否是递增或者递减序列，然后求得最小值；通过
# 二分查找改变left和right值。
#