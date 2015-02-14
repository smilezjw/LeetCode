# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def trap(self, A):
        water = 0
        # 开辟数组，记录i之前的最高高度
        leftmosthigh = [0 for i in xrange(len(A))]
        leftmax = 0
        rightmax = 0
        for i in xrange(len(A)):
            if A[i] > leftmax:
                leftmax = A[i]
            leftmosthigh[i] = leftmax  #i之前最高的高度
        for i in reversed(xrange(len(A))):  # 从后往前遍历
            if A[i] > rightmax:
                rightmax = A[i]  # 从后往前遍历，记录i位置后面最高的高度
            # 如果i位置前面和后面的高度都高于当前位置的高度，则该位置能够储水，
            # 储水量为min(leftmosthigh[i], rightmax) - A[i]
            elif min(rightmax, leftmosthigh[i]) > A[i]:
                water += min(rightmax, leftmosthigh[i]) - A[i]
        return water

if __name__ == '__main__':
    s = Solution()
    print s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print s.trap([4, 2, 3])
    print s.trap([4, 4, 4, 7, 1, 0])
    print s.trap([2, 1, 0, 2])

#############################################################################################
# 这道题目还是很有意思的，主要考虑当前位置的前面和后面的最高位置，如果前后的最高位置都高于
# 当前位置，则可以储水。
# 在写代码时，开辟一个新的数组用于记录i位置前面的最高位置，然后从后往前遍历，同时记录当前位置
# 后面的最高位置，判断前后最高位置是否都高于当前位置，计算储水量。这种思路的时间复杂度为O(n)。
#