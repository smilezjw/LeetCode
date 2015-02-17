# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def rotate(self, matrix):
        dim = len(matrix)
        res = [[0 for i in xrange(dim)] for j in xrange(dim)]
        for j in xrange(dim):                # 原来矩阵的纵坐标旋转后变成横坐标，依然从小到大
            for i in reversed(xrange(dim)):  # 原来矩阵的横坐标旋转后变成纵坐标，从大到小
                # 找到旋转后矩阵坐标和原始坐标之间的关系，i和j互换，i现在是从大到小，把它再换回从小到大
                res[j][dim-i-1] = matrix[i][j]
        return res

if __name__ == '__main__':
    s = Solution()
    matrix = [[00, 01, 02, 03],
             [10, 11, 12, 13],
             [20, 21, 22, 23],
             [30, 31, 32, 33]]
    print s.rotate(matrix)

###########################################################################################
# 我做这道题的思路是，先找到旋转后矩阵坐标和原始坐标之间的关系：原来的纵坐标变成横坐标，
# 保持从小到大；原来的横坐标变成纵坐标，从大到小。初始化一个矩阵，然后对应这个规律，把旋转后
# 矩阵的值按照对应的坐标赋给初始化矩阵。
#