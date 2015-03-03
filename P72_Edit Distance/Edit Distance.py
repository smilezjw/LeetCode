# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def minDistance(self, word1, word2):
        m = len(word1) + 1
        n = len(word2) + 1
        # 用二维数组表示dp[i][j]表示word1[0...i-1]到word[0...j-1]的编辑距离
        dp = [[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(n):
            dp[0][i] = i  # dp[0][i] = i 因为需要做i次添加操作
        for i in xrange(m):
            dp[i][0] = i  # dp[i][0] = i 因为需要做i次删除操作
        for i in xrange(1, m):
            for j in xrange(1, n):
                # 状态转移方程
                dp[i][j] = min(1 + dp[i-1][j], dp[i][j-1] + 1,
                               dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))
        return dp[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    print s.minDistance('min', 'man')

##########################################################################################
# 这道题是很有名的编辑距离问题，用动态规划求解。
# 用二维数组表示状态，dp[i][j]表示word1[0...i-1]到word[0...j-1]的编辑距离。
# 状态转移方程的初始状态：dp[0][i] = i 因为需要做i次添加操作；
#                         dp[i][0] = i 因为需要做i次删除操作。
# 如果word1[i-1] == word2[j-1]，那么dp[i-1][j-1] == dp[i][j]，否则：
# （1）把word1前i-1个字符变成word2的前j-1个字符，然后再把word1的第i个字符变成word2的第j个
#      字符，即dp[i][j] = dp[i-1][j-1] + 1;
# （2）把word1前i个字符变成word2的前j-1个字符，然后再加上word2的第j个字符，
#      即dp[i][j] = dp[i][j-1] + 1;
# （3）删掉word1第i个字符，然后把word1的前i-1个字符变成word2的前j个字符，
#      即dp[i][j] = 1 + dp[i][j-1];
# 取三种情况中的最小值，求得最后最小的编辑距离。
#