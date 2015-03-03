# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        rows = [False for i in xrange(m)]      # 如果该行有0则该行为True
        columns = [False for j in xrange(n)]   # 如果该列有0则该列为True
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    columns[j] = True
        for i in xrange(m):                   # 第二次遍历时，将对应的行和列全部修改为0
            for j in xrange(n):
                if rows[i] or columns[j]:
                    matrix[i][j] = 0
        return matrix


if __name__ == '__main__':
    matrix = [[1,2,3,0],
              [0,4,5,6],
              [7,8,9,2]]
    s = Solution()
    print s.setZeroes(matrix)

##########################################################################################
# 这道题要求不引入额外的存储空间，只能在原来的数组上进行修改。进行两次遍历，第一次遍历
# 遇到0则将对应的行和列标记为True。第二次遍历将对应的行和列的值修改为0。
#