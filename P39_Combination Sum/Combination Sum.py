# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()  # 先对候选数字进行排序
        Solution.res = []  # 初始化全局变量
        self.dfsSum(candidates, target, 0, [])
        return Solution.res

    def dfsSum(self, candidates, target, start, temp):  # 深度优先搜索
        if target == 0:
            Solution.res.append(temp)
        for i in xrange(start, len(candidates)):
            if candidates[i] > target:  # 如果候选数字已经大于target，则剪枝
                return
            # 注意这里从i开始搜索，这里用temp.append(candidates[i])会报错
            self.dfsSum(candidates, target - candidates[i], i, temp + [candidates[i]])

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2, 3, 6, 7], 7)

###############################################################################################
# 这道题用深度优先搜索，递归遍历所有可能解。注意每次都从当前查找的位置递归遍历下去，而不是i+1。
# 这道题貌似还可以用动态规划做= =
#