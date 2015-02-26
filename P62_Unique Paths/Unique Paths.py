# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def uniquePaths(self, m, n):  # 动态规划
        if m == 1 and n == 1:
            res = [[1]]
        elif m == 1 and n > 1:
            res = [[1 for i in xrange(n)]]
        elif m > 1 and n == 1:
            res = [[1] for j in xrange(m)]
        else:
            res = [[0 for j in xrange(n)] for i in xrange(m)]
            for j in xrange(n):
                res[0][j] = 1
            for i in xrange(m):
                res[i][0] = 1
            for i in xrange(1, m):
                for j in xrange(1, n):
                    #                         向下走         向右走
                    # 状态转移方程 dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    print s.uniquePaths(1,2)

###########################################################################################
# 这道题采用动态规划的方法来做，状态转移方程容易理解，因为只能向右走或向下走，因此列出状态转
# 移方程；然后判断各个边界条件。这道题还可以不用动态规划方法解决。
#