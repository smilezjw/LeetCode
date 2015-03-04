# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def combine(self, n, k):
        Solution.res = []
        Solution.count = 0
        self.dfs(n, k, 1, [])
        return Solution.res

    def dfs(self, n, k, start, valueList):  # 求组合的问题，这里用DFS来解决
        if Solution.count == k:              # count记录valueList中元素个数
            Solution.res.append(valueList)
            return
        for i in xrange(start, n+1):
            Solution.count += 1
            self.dfs(n, k, i+1, valueList + [i])
            Solution.count -= 1              # 每次从递归中返回，则valueList中元素个数少1个
        return

if __name__ == '__main__':
    s = Solution()
    print s.combine(4, 2)

################################################################################################
# 每次这种递归的题目都做不好。这道题用深度优先搜索求解。用变量count来记录列表中元素个数，用来
# 判断返回条件。注意每次从递归中返回，count都要减1，因为里面元素个数少1个了。如果当前位置的元素
# 都遍历完了，这时候也要从递归中返回。
# 做递归的题目还是需要判断返回条件和传入的参数。