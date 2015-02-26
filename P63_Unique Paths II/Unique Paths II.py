# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in xrange(m):
            for j in xrange(n):
                obstacleGrid[i][j] = 1 - obstacleGrid[i][j]  # 先将0和1都反转过来
        for i in xrange(m):
            if obstacleGrid[i][0] == 0:    # 对于第0列，如果遇到障碍，则后面都设置为0，因为过不去了
                for j in xrange(i+1, m):
                    obstacleGrid[j][0] = 0
                break
        for j in xrange(n):
            if obstacleGrid[0][j] == 0:   # 对于第0行也是，如果遇到障碍，该行后面都设置为0
                for i in xrange(j+1, n):
                    obstacleGrid[0][i] = 0
                break
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 0:  # 遇到障碍不能走
                    continue
                else:  # 根据状态转移方程计算
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    obstacleGrid1 = [[0,0,0],
                    [0,1,0],
                    [0,0,0]]
    obstacleGrid2 = [[0]]
    obstacleGrid3 = [[1]]
    print s.uniquePathsWithObstacles(obstacleGrid3)

##########################################################################################
# 这道题和62题是差不多的思路，都采用动态规划求解。这道题更加麻烦的是对于障碍走不过，该格中
# 路径书设置为0。
#