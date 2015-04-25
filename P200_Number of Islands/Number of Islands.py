# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def numIslands(self, grid):
        Solution.grid = grid
        num = 0
        for i in xrange(len(Solution.grid)):
            for j in xrange(len(Solution.grid[0])):
                if Solution.grid[i][j] == '1':      # 找到1，即找到一个岛屿
                    num += 1
                    self.dfs(i, j)                  # 深度递归，找邻接的lands
        return num

    def dfs(self, i, j):
        if 0 <= i < len(Solution.grid) and 0 <= j < len(Solution.grid[0]) and Solution.grid[i][j] == '1':
            Solution.grid[i][j] = '#'  # 用#表示是否被访问过
            self.dfs(i-1, j)           # 然后遍历其上下左右相邻的点判断是否为同一片岛屿
            self.dfs(i+1, j)
            self.dfs(i, j-1)
            self.dfs(i, j+1)

if __name__ == '__main__':
    s = Solution()
    grid = [['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']]
    grid2 = [['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0']]
    print s.numIslands(grid2)

######################################################################################
# 这道题用深度优先遍历完成。遍历二维数组，找打一个1后计数，然后深度遍历其上下左右邻接
# 的点判断是否为1，并且用#表示已经遍历过。这样子同一个岛屿只被计数一次。
#
