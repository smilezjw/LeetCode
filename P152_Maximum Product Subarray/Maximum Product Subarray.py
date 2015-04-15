# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def maxProduct(self, A):
        # 本来想用数组记录当前位置后面还有多少个负数，但是这种方法在对curr等变量赋值时存在问题，还是不对的
        # length = len(A)
        # if length == 1:
        #     return A[0]
        # negative = [0 for i in xrange(length + 1)]
        # negative[-1] = -1
        # res = - 2** 31
        # curr = 1
        # for i in xrange(length-1, -1, -1):
        #     if A[i] < 0:
        #         negative[i] = negative[i+1] + 1
        #     else:
        #         negative[i] = negative[i+1]
        # for i in xrange(length):
        #     if A[i] == 0 or (A[i] < 0 and negative[i] == 0 and curr > 0):
        #         res = max(res, A[i])
        #         curr = 1
        #     else:
        #         curr *= A[i]
        # res = max(res, curr)
        # return res

        # mintemp变量保存局部最小值，只有当这个局部最小值是负数时，遇到下一个负数才起作用
        # maxtemp变量保存局部最大值
        mintemp = maxtemp = res = A[0]
        for i in xrange(1, len(A)):
            curr = [A[i], mintemp * A[i], maxtemp * A[i]]
            mintemp = min(curr)  # 更新局部最小值
            maxtemp = max(curr)  # 更新局部最大值
            res = max(maxtemp, res)
        return res

if __name__ == '__main__':
    s = Solution()
    A = [2, 3, -2, 4]
    B = [2, 3, 0, -2, 4, -2]
    C = [-2, 0, -1]
    print s.maxProduct(C)

#########################################################################################
# 这道题和P53题思路类似，由于负负得正的情况可能存在，因此需要两个变量分别记录当前局部最小
# 值和局部最大值，只有当局部最小值为负数时才有意义。
# 这道题有动态规划的思想在里面，需要找到局部和全局的递推关系。
#