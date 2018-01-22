# coding=utf8

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row-1):
            for j in range(column-1):
                num = matrix[i][j]
                if i+1 < row and j+1 < column and matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    matrix0 = [[1, 2, 3, 4],
              [5, 1, 2, 3],
              [9, 5, 1, 2]]
    print(sol.isToeplitzMatrix(matrix0))

    matrix1 = [[1, 2],
               [2, 2]]
    print(sol.isToeplitzMatrix(matrix1))
