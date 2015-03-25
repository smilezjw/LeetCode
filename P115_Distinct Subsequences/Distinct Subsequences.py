# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def numDistinct(self, S, T):
        lenT = len(T)
        lenS = len(S)
        # dp[i][j]表示T[:j]是S[:i]子串的数量
        dp = [[0 for j in xrange(lenT+1)] for i in xrange(lenS+1)]
        # 初始化状态：空串是任意字符串的子串
        for i in xrange(lenS+1):
            dp[i][0] = 1
        for i in xrange(lenS):
            for j in xrange(min(lenT, i+1)):
                # 如果S[i]==T[j]，那么S[:i+1]中有多少子串是T[:j+1]表示：
                # S[:i]中有多少子串是T[:j], 并且S[:i]中有多少子串是T[:j+1]
                # 因为子串的定义是从S中删去若干个字符得到T
                if S[i] == T[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                # 如果S[i]！=T[j]，那么看S[:i]中有多少子串是T[j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[lenS][lenT]

if __name__ == '__main__':
    s = Solution()
    print s.numDistinct('b', 'b')
    print s.numDistinct('eee', 'eee')
    print s.numDistinct('rabbbit', 'rabbit')

####################################################################################
# 这道题主要还是要理解题目意思，还有需要注意初始化条件：空串是任意字符串的子串。
# 子串的定义是从S中删除若干个字符得到T，因此还要考虑d[i][j+1]的情况。
#