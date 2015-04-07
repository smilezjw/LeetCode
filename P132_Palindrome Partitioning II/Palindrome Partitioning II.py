# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # Time Limit Exceed
    def minCut_dfs(self, s):
        Solution.res = 2 ** 31 - 1
        self.partition(s, 0)
        return Solution.res

    def partition(self, s, cut):
        if len(s) == 0:
            Solution.res = min(Solution.res, cut - 1)
        for i in xrange(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.partition(s[i:], cut + 1)

    def isPalindrome(self, s):
        for i in xrange(len(s)):
            if s[i] != s[-(i+1)]:
                return False
        return True

    def minCut_DynamicProgramming(self, s):
        dp = [i + 1 for i in xrange(len(s))]
        isPal = [[False for i in xrange(len(s))] for j in xrange(len(s))]
        for i in xrange(len(s)):
            for j in reversed(xrange(i+1)):
                if s[i] == s[j] and ((i - j) < 2 or isPal[j + 1][i - 1]):
                    isPal[j][i] = True
                    if j > 0:
                        dp[i] = min(dp[j-1] + 1, dp[i])
                    else:
                        dp[i] = min(dp[i], 1)
        return dp[-1] - 1

if __name__ == '__main__':
    s = Solution()
    # print s.minCut_DynamicProgramming('leet')
    # print s.minCut_DynamicProgramming('ab')
    # print s.minCut_DynamicProgramming('a')
    # print s.minCut_DynamicProgramming('bb')
    print s.minCut_DynamicProgramming('aab')

######################################################################################
# 上一题P131是穷举所有符合条件的解，需要用深度优先遍历解法求解；这道题是求最小的解
# 的个数，那应该是用动态规划做。这样的思路还是应该想得到的。
#
#