# coding=utf8

__author__ = 'smilezjw'

class Solution:
    def jump(self, A):
        length = len(A)
        if length == 1:
           return 0
        maxLen = 0
        steps = 0
        i = 0
        while i < length:
            maxLen = max(maxLen, i + A[i])
            if maxLen > 0:
                steps += 1
            if maxLen >= length - 1:
                return steps
            temp = 0
            # 找到从位置i开始目前能够达到最大的位置范围内，能够继续接着跳到的最大范围，总是找最大范围
            for j in xrange(i+1, maxLen+1):
                if j+A[j] > temp:
                    temp = j + A[j]
                    i = j  # 找到最大范围，然后跳到这一步

if __name__ == '__main__':
    s = Solution()
    print s.jump([2, 3, 1, 1, 4])
    print s.jump([1])
    print s.jump([1, 2])
    print s.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])

###########################################################################################
# 这道题用贪心法，每次跳的步数保证是目前能够达到的最大范围，因此需要在当前可以跳的最长距离
# 内判断下一跳是否能够达到最大范围。这道题的目的是找到最少步数，因此保证每一跳都能使总的距
# 离尽可能远。
#