# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def subsets(self, S):
        Solution.count = 0
        Solution.res = []
        for k in xrange(len(S)+1):  # k表示子集中元素个数，最多len(S)
            self.dfs(S, k, 0, [])
        return Solution.res

    def dfs(self, S, k, start, valueList):
        if Solution.count == k:
            Solution.res.append(sorted(valueList))  # 子集中元素按非降序排序
            return
        for i in xrange(start, len(S)):
            if S[i] not in valueList:
                Solution.count += 1  # 子集中加入一个元素， count+1
                self.dfs(S, k, i+1, valueList + [S[i]])  # 然后加入下一个元素
                Solution.count -= 1
        return

if __name__ == '__main__':
    s = Solution()
    print s.subsets([1, 2, 3])
    print s.subsets([4, 1, 0])

##############################################################################################
# 这道题的解题思路和第77题是类似的，77题给定子集中元素个数，求出相应的子集；而这道题是给定列表
# 元素，求出所有的子集。那么在77题的基础上，求出不同元素个数的子集，也就是多加一步，k表示子集
# 中元素个数，k从0到列表长度，求出所有k长度的子集，子集中元素按照非降序排列。 同样采用DFS求解。
# 另外，子集不是多重集，即子集中不存在重复元素。