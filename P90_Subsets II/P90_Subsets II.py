# coding=utf8

__author__ = 'dell'


class Solution:
    def subsetsWithDup(self, S):
        S = sorted(S)  # 由于子集中元素要求非降序排列，因此这里先对列表S排序
        Solution.res = []
        Solution.count = 0  # 记录子集中元素个数
        for k in xrange(len(S)+1):  # 子集中元素个数从0到len(S)
            self.dfs(S, k, 0, [])
        return Solution.res

    def dfs(self, S, k, start, valueList):
        if Solution.count == k and valueList not in Solution.res:  # 子集去重
            Solution.res.append(valueList)
            return
        for i in xrange(start, len(S)):
            Solution.count += 1
            self.dfs(S, k, i+1, valueList + [S[i]])
            Solution.count -= 1
        return

if __name__ == '__main__':
    s = Solution()
    print s.subsetsWithDup([1, 2, 2])

##########################################################################################
# 这道题和第77、78题的解题思路类似，都是用深度优先搜索递归求解。这里由于集合中元素可能重复，
# 因此需要子集中需要去重。
#