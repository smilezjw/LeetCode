# coding=utf8

__author__ = 'smilezjw'

import re

class Solution(object):
    def diffWaysToCompute(self, input):
        def cal(a, b, op):
            return {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}[op](a, b)
        def dfs(nums, ops):
            if not ops:
                return [nums[0]]
            ans = []
            # 循环拆分
            for x in xrange(len(ops)):
                # 将表达式按照运算符递归地拆分为左右两部分
                left = dfs(nums[:x+1], ops[:x])
                right = dfs(nums[x+1:], ops[x+1:])
                # 左右两部分有不同的计算出来的值，因此要用列表
                for l in left:
                    for r in right:
                        ans.append(cal(l, r, ops[x]))
            return ans
        nums, ops = [], []
        # If capturing parentheses are used in pattern, then the text of all groups in the pattern
        # are also returned as part of the resulting list.
        # \D matches any non-digit character, equivalent to [^0-9]
        input = re.split(r'(\D)', input)
        print input
        for x in input:
            if x.isdigit():
                nums.append(int(x))
            else:
                ops.append(x)
        return dfs(nums, ops)


if __name__ == '__main__':
    s = Solution()
    print s.diffWaysToCompute('2*3-4*5')

#######################################################################################
# 这道题还是有一定难度的，参考了人家的解法，调试着走下来，还有更简洁的，学习。
#
