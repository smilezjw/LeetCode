# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 单纯用DFS深搜会超时Time Limit Exceeded
    def wordBreak(self, s, dict):
        Solution.res = []
        self.dfs(s, dict, [], 0, 1)
        return Solution.res

    def dfs(self, s, dict, valueList, k, i):
        if self.canBreak(s, dict):
            if i == len(s) + 1:
                Solution.res.append(' '.join(valueList))
                return
            while i < len(s) + 1:
                if s[k:i] in dict:
                    self.dfs(s, dict, valueList + [s[k:i]], i, i+1)
                i += 1

    # 在进行深搜求解之前，先判断是否有解
    def canBreak(self, s, dict):
        dp = [False for i in xrange(len(s)+1)]
        dp[0] = True
        for i in xrange(1, len(s)+1):
            for k in xrange(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('a', ['a'])
    print s.wordBreak('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog'])

###########################################################################################
# 这道题一开始直接用DFS求解会超时，需要用动态规划的解法先判断是否有解，如果有解在用深搜进行
# 求解。动态规划的解法就和上一题一模一样。原来这就是Dynamic Programming + DFS 啊！
#
