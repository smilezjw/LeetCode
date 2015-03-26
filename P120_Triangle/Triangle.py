# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def minimumTotal(self, triangle):
        rowNum = len(triangle)
        for i in xrange(1, rowNum):
            for j in xrange(len(triangle[i])):
                # 如果是第0个元素，则只由上一行的第0个元素走过来
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                # 如果是第1到该行最后第2个元素，那可以由上一行的j或者j-1这两个元素过来，取其中的最小值
                elif 0 < j < len(triangle[i]) - 1:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
                # 如果是最后一个元素，那么只由上一行的最后一个元素j-1走过来
                else:
                    triangle[i][j] += triangle[i-1][j-1]
        # 动态改变三角中的值，取到最后一行中最小的元素就是路径上最小的和
        return min(triangle[rowNum-1])

if __name__ == '__main__':
    s = Solution()
    triangle1 = [[-1],[2,3],[1,-1,-3]]
    triangle2 = [[2],
                [3,4],
                [6,5,7],
                [4,1,8,3]]
    print s.minimumTotal(triangle2)

###################################################################################
# 我觉得这道题的难点还是在于需要理解“每一步只能走到下一行的相邻元素”中的“相邻的
# 含义”， 并不是j-1，j, j+1三个元素都可以，而是从形状上看上去是邻接的，也就是代码中
# 的三个if判断条件。
# 使用动态规划更新每一行的数字，取到最后一行中最小元素，就是路径上最小和。