# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] == target:
                return True
            elif A[left] < A[mid]:    # 旋转的部分在mid右边
                if A[left] <= target < A[mid]:  # left和mid之间的数字是有序的
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[left] > A[mid]:    # 旋转的部分在mid左右
                if A[mid] < target <= A[right]:  # mid和right之间的数字是有序的
                    left = mid + 1
                else:
                    right = mid - 1
            else:    # 如果left == mid, left增加一位
                left += 1
        return False

if __name__ == '__main__':
    s = Solution()
    print s.search([3, 1], 1)
    print s.search([1, 3, 1], 1)

#############################################################################################
# 这道题虽然要求比第33题稍微复杂一点，但是算法可以是一样的，主要是在处理边界的时候考虑的情况。
# 如果旋转的部分在左边，那么mid右边的数字是有序的；如果旋转的部分在右边，那么mid左边的数字是有
# 序的；如果A[left] == A[mid]，由于A[mid] != target, 那么left向右移一位即可。 无论列表中的元素
# 是否有重复，这个思路是通用的。
#