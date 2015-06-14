# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = abs(C - A) * abs(D - B)
        area2 = abs(G - E) * abs(F - H)
        # 需要考虑到两个矩形完全不相交的情况
        if E >= C or F >= D or G <= A or H <= B:
            return area1 + area2
        # 两个矩形有相交的情况，甚至是包含关系
        else:
            x_bottom = max(A, E)
            y_bottom = max(B, F)
            x_top = min(C, G)
            y_top = min(D, H)
            return area1 + area2 - abs(x_top - x_bottom) * abs(y_top - y_bottom)

if __name__ == '__main__':
    s = Solution()
    print s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
    print s.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
    print s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
    print s.computeArea(-2, -2, 2, 2, -4, 3, -3, 4)

########################################################################################
# 这道题需要画图，尤其是两个矩形完全不想交以及包含的两种特殊情况。
#