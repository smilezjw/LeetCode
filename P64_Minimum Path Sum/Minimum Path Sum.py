# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in xrange(1, m):
            grid[i][0] += grid[i-1][0]  # 对第0列进行处理
        for j in xrange(1, n):
            grid[0][j] += grid[0][j-1]  # 对第0行进行处理
        for i in xrange(1, m):
            for j in xrange(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])  # 动态规划，状态转移方程
        return grid[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    grid = [[1,2],[1,1]]
    print s.minPathSum(grid)

#########################################################################################
# 动态规划，这道题和第62题比较类似，每一步都要取向右走或向下走的最短数字和。
#