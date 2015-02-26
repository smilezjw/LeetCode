# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def climbStairs(self, n):
        if n == 1:
            res = [1]
        else:
            res = [0 for i in xrange(n)]
            res[0] = 1  # 第一个台阶只有一种走法
            res[1] = 2  # 第二个台阶有两种走法：一步一步走两次，一次性走两步
            for i in xrange(2, n):
                # 状态转移方程，先走完n-1个台阶，然后走一步；或者走完n-2个台阶，然后走两步
                res[i] = res[i-1] + res[i-2]
        return res[n-1]

if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(3)

##########################################################################################
# 这道题其实是斐波那契额数列的求解。逆向分析，有n个台阶，走完n个台阶有两种方法，先走完n-1
# 个台阶然后走一步，或者是走完n-2个台阶然后一次走两步。用动态规划，列出状态转移方程。
#