# coding=utf8

__author__ = 'smilezjw'

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        Solution.res = []
        self.dfsSum2(candidates, target, 0, [])
        return Solution.res

    def dfsSum2(self, candidates, target, start, temp):
        # 注意这里需要去重，因为候选数字集里有重复数字
        if target == 0 and temp not in Solution.res:
            Solution.res.append(temp)
        for i in xrange(start, len(candidates)):
            if candidates[i] > target:
                return
            # 由于每个数字最多只能使用一次，因此这里递归的时候需要从i+1开始
            self.dfsSum2(candidates, target - candidates[i], i+1, temp + [candidates[i]])

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5], 8)

############################################################################################
# 这道题和上一道39题思路是一样的，都使用深度优先遍历。区别在于上一道题每个数字可以无限次
# 使用，因此递归时从当前位置i开始深度遍历；而这道题每个数字最多只能使用一次，因此递归时
# 要从i+1开始，而且还需要避免重复解，因为候选数字集合里面可能会有重复数字。其他的思路和
# 写法都是一样的。
#