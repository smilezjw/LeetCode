# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def largestRectangleArea(self, height):
        i = 0
        stack = []
        area = 0
        while i < len(height):
            if stack == [] or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                if stack == []:
                    width = i
                else:
                    width = i - 1 - stack[-1]
                area = max(area, width * height[curr])
                i -= 1
            i += 1
        while stack != []:
            curr = stack.pop()
            if stack == []:
                width = i
            else:
                width = i - 1 - stack[-1]
            area = max(area, width * height[curr])
        return area

    def maximalRectangle(self, matrix):
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        maxArea = 0
        a = [0 for i in xrange(n)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    a[j] += 1    # 注意对每一行的处理
                else:
                    a[j] = 0
            maxArea = max(maxArea, self.largestRectangleArea(a))  # 对每一行利用上一题的思路求得该行最大矩形区域面积
        return maxArea

if __name__ == '__main__':
    s = Solution()
    matrix = ["1101","1101","1111"]
    print s.maximalRectangle(matrix)

##############################################################################################
# 这题果然精巧。利用上一题的解法，对矩阵每一行都求得最大矩形区域面积，如果是1则该列数值加1，
# 否则该列为0。
#