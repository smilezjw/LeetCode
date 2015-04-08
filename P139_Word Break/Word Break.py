# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def wordBreak(self, s, dict):
        # Runtime Error
        if len(dict) == 0:
            return False
        return self.dfs(s, dict, 0, len(s) - 1)

    # Runtime Error
    def dfs(self, s, dict, i, j):
        if i > j:
            return True
        if s[i:j+1] in dict:
            if self.dfs(s, dict, j+1, len(s)-1):
                return True
        elif s[i:j+1] != '':
            if self.dfs(s, dict, i, j-1):
                return True
        return False

    # Time Limit Exceed
    # 其实还是在遍历每一种可能性，时间复杂度O(n**2)
    def wordBreak_DynamicProgramming(self, s, dict):
        if len(dict) == 0:
            return False
        length = len(s)
        dp = [False for i in xrange(length)]
        pos = [-1]
        while len(pos) > 0:
            i = pos.pop(0) + 1
            for j in xrange(i, length):
                if s[i:j+1] in dict:
                    dp[j] = True
                    pos.append(j)
            if i >= length and dp[-1]:
                return True
        return False

    def wordBreak_DP(self, s, dict):
        dp = [False for i in xrange(len(s) + 1)]  # dp[i]记录在位置i之前的字符串是否都在dict中匹配
        dp[0] = True  # 初始化，空串可以匹配
        for i in xrange(1, len(s)+1):  # 注意i的起始范围
            for k in xrange(i):        # k来缩减字符串的长度
                # 如果k位置之前的字符串都已经匹配了，并且s[k:i]在dict中匹配，则记录为True
                # 如果k位置之前的字符串都没有匹配，则必须找到k前面的字符串也能匹配的位置才行
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak_DP('bb', ['a', 'b', 'bbb', 'bbbb'])
    print s.wordBreak_DP('a', [])
    print s.wordBreak_DP('aaaaaaa', ['aaaa', 'aaa'])
    print s.wordBreak_DP('leetcode', ['leet','code'])
    print s.wordBreak_DP('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ['a', 'aa', 'ba'])

##############################################################################################
# 这道题只需要判断是否可以分割单词，不需要给出如何分割的解，因此考虑用动态规划求解。遍历整个
# 字符串，考虑每个位置之前的字符串是否都在dict中匹配，用k变量来移动字符串的长度。如果k位置前
# 的字符串都已经匹配，并且s[k:i]的字符串也能够匹配，那么i位置的状态设置为True。
#
