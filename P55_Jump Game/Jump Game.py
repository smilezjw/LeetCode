# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def canJump(self, A):
        length = len(A)
        maxLen = 0
        for i in xrange(length):
            if i > maxLen:  # 如果最大距离已经能够达到i位置了，才能接着跳；否则直接返回False
                return False
            maxLen = max(maxLen, i + A[i])
            if maxLen >= length - 1:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print s.canJump([2, 3, 1, 1, 4])
    print s.canJump([3, 2, 1, 0, 4])
    print s.canJump([1, 0, 6, 0, 0, 1])

############################################################################################
# 理解这道题目花了好久时间，这道题目的意思是：一开始从0位置出发，列表A[i]表示位置i上可以跳的
# 最大步长；如果某个位置前的最大范围小于该位置，也就是说不能跳到该位置了，那么直接结束；判断
# 结果是否能够跳到最后一个位置len(A)-1。所以这里要判断i<=maxLen，否则游戏直接结束了。如果最大
# 范围大于最后一个位置，那是可以达到该位置的。