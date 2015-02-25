# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def generateMatrix(self, n):
        matrix = [[-1 for i in xrange(n)] for j in xrange(n)]  # 初始化方阵
        up = 0
        left = 0
        right = n-1
        down = n-1
        direction = 0  # 0-- go right  1-- go down  2-- go left  3-- go up
        count = 1  # 要填充的数字
        total = n ** 2
        while count <= total:
            if direction == 0:  # from left to right
                for j in xrange(left, right+1):
                    matrix[up][j] = count
                    count += 1
                up += 1
            if direction == 1:  # from up to down
                for i in xrange(up, down+1):
                    matrix[i][right] = count
                    count += 1
                right -= 1
            if direction == 2:  # from right to left
                for j in xrange(right, left-1, -1):
                    matrix[down][j] = count
                    count += 1
                down -= 1
            if direction == 3:  # from down to up
                for i in xrange(down, up-1, -1):
                    matrix[i][left] = count
                    count += 1
                left += 1
            direction = (direction + 1) % 4
        return matrix

if __name__ == '__main__':
    s = Solution()
    print s.generateMatrix(3)

##########################################################################################
# 这道题和第54题类似，54题是将矩阵的数字按照螺旋顺序读取出来，这道题是按照螺旋顺序将n^2个
# 数字写入方阵中，一样的思路几乎一样的代码。
#