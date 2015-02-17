# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def spiralOrder(self, matrix):  # 自己写的算法也可以过，就是比较复杂
    #     Solution.res = []
    #     self.spiral(matrix, 0, 0)
    #     return Solution.res
    #
    # def spiral(self, matrix, i, j):
    #     m = len(matrix)
    #     if m == 0:
    #         return
    #     n = len(matrix[0])
    #     if n == 0:
    #         return
    #     if m == 1 and n > 1:
    #         Solution.res += matrix[0]
    #         return Solution.res
    #     if m > 1 and n == 1:
    #         for x in xrange(m):
    #             Solution.append(matrix[x][0])
    #         return Solution.res
    #     if m == n == 1:
    #         Solution.res.append(matrix[0][0])
    #         return Solution.res
    #     while j < n-1:  # 从左到右
    #         Solution.res.append(matrix[0][j])
    #         j += 1
    #     while i < m-1:  # 从上到下
    #         Solution.res.append(matrix[i][j])
    #         i += 1
    #     while j > 0:    # 从右到左
    #         Solution.res.append(matrix[i][j])
    #         j -= 1
    #     while i > 0:    # 从下到上
    #         Solution.res.append(matrix[i][j])
    #         i -= 1
    #     temp = []
    #     for i in xrange(1, m-1):  # 更新剩下的矩阵
    #         tmp = []
    #         for j in xrange(1, n-1):
    #             tmp.append(matrix[i][j])
    #         temp.append(tmp)
    #     self.spiral(temp, 0, 0)   # 递归进行螺旋处理
    #     return Solution.res

    def spiralOrder(self, matrix):
        if matrix == []:
            return matrix
        up = 0
        left = 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1
        direct = 0  # 0-- go right  1-- go down  2-- go left  3-- go up
        res = []
        while True:
            if direct == 0:
                for j in xrange(left, right+1):  # from left to right
                    res.append(matrix[up][j])
                up += 1
            if direct == 1:
                for i in xrange(up, down+1):    # from up to down
                    res.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for j in xrange(right, left-1, -1):  # from right to left
                    res.append(matrix[down][j])
                down -= 1
            if direct == 3:
                for i in xrange(down, up-1, -1):    # from down to up
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right:  # 退出循环的出口
                return res
            direct = (direct + 1) % 4     # 精彩之处在这里呢，一共4个方向嘛

if __name__ == '__main__':
    s = Solution()
    matrix = [[ 1, 2, 3 ],
              [ 4, 5, 6 ],
              [ 7, 8, 9 ]]
    matrix2 = [[6, 9, 7]]
    matrix3 = [[7],
               [9],
               [6]]
    matrix4 = [[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]]
    print s.spiralOrder(matrix4)

###########################################################################################
# 这道题没有tricky的方法，但是人家精彩的写法非常好理解，还是需要多学习！
#