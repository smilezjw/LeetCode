# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def searchMatrix(self, matrix, target):
        i = 0
        j = len(matrix) - 1
        cols = len(matrix[0]) - 1
        while i <= j:
            mid = (i + j) / 2
            if matrix[mid][0] <= target <= matrix[mid][cols]:  # 先二分查找找到target的范围对应哪一行
                p = 0
                q = cols
                while p <= q:                                 # 然后在对应行里二分查找是否有target
                    mmid = (p + q) / 2
                    if matrix[mid][mmid] == target:
                        return True
                    elif matrix[mid][mmid] > target:
                        q = mmid - 1
                    else:
                        p = mmid + 1
                return False
            elif matrix[mid][cols] < target:
                i = mid + 1
            elif matrix[mid][0] > target:
                j = mid - 1
        return False

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]
    matrix2 = [[1, 3, 5]]
    print s.searchMatrix(matrix, target=2)
    print s.searchMatrix(matrix2, target=4)

##############################################################################################
# 我用了两次二分查找，首先判断target在哪一行的范围内，然后在对应行里二分查找是否存在target。
#