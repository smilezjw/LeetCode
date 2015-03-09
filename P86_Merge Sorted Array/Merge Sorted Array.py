# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def merge(self, A, m, B, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] < B[j]:
                A[k] = B[j]
                j -= 1
            else:
                A[k] = A[i]
                i -= 1
            k -= 1
        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1
        return A

if __name__ == '__main__':
    s = Solution()
    print s.merge([1, 3, 5, 7, 8, 0, 0, 0, 0], 5, [2, 4, 6, 9], 4)

###########################################################################################
# 这道题题目意思是A列表本身长度至少为m+n，前面m个元素是初始化过的，所以如果从头开始判断大小
# 归并，需要每次计算列表A的实际长度，那就有问题了。所以这道题为了避免每次计算列表A的实际长
# 度，从后往前归并。机智啊！
#