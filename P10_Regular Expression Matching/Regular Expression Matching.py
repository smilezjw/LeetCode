# coding=utf8

__author__ = 'smilezjw'


import re

class Solution:
    def isMatch(self, s, p):
        return re.match('^' + p +'$', s) != None


    def isMatch_DP(self, s, p):
        # dp[i][j]表示字符串s[:i]和p[:j]是否匹配
        dp = [[False for i in xrange(len(p)+1)] for j in xrange(len(s)+1)]
        # 两个空串必然匹配
        dp[0][0] = True
        # 例如s='', p='a*'是可以匹配的，因为*可以匹配0个或多个
        for i in xrange(1, len(p)+1):
            if p[i-1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i-2]
        # 状态转移方程，从头开始遍历s和p字符串
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                # 如果遇到'.'，则默认s[i-1]和p[j-1]匹配
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                # 如果遇到'*',则考虑*是重复0个字符、1个字符还是多个字符
                # 如果*重复0个字符，则dp[i][j] = dp[i][j-2]
                # 如果*重复1个字符，则dp[i][j] = dp[i][j-1]
                # 如果*重复多个字符，则dp[i][j] = dp[i-1][j] and s[i-1] == p[j-2] or p[j-2] == '.'，
                # 就是判断是否一直在重复*前面的那个字符，这里p[j-2]是*号前面一个字符，不要搞错了
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                # 否则就是前一个状态并且当前s[i-1]和p[j-1]是否匹配
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        # 返回dp[-1][-1]就是最后s和p两个字符串是否匹配的结果
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.isMatch('aa', 'a')
    print s.isMatch('aa', 'aa')
    print s.isMatch('aa', 'a*')
    print s.isMatch('aa', '.*')
    print s.isMatch('aab', 'c*a*b')

    print s.isMatch_DP('aa', 'a')
    print s.isMatch_DP('aa', 'aa')
    print s.isMatch_DP('aa', 'a*')
    print s.isMatch_DP('aa', '.*')
    print s.isMatch_DP('aab', 'c*a*b')