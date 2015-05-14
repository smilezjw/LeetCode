# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def sortColors(self, A):
    #     res = {}
    #     result = []
    #     for i in xrange(len(A)):
    #         if A[i] not in res:
    #             res[A[i]] = [i]
    #         else:
    #             res[A[i]].append(i)
    #     for j in [0, 1, 2]:
    #         for i in res[j]:
    #             result.append(A[i])
    #     return result

    def sortColors(self, A):
        if len(A) == 0:
            return A
        length = len(A)
        p0 = 0           # p0指向0该放的位置
        p2 = length - 1  # p2指向2该放的位置
        i = 0            # i遍历整个数组
        while i <= p2:
            if A[i] == 2:  # 遇到2则把2和p2指向的数交换
                A[i], A[p2] = A[p2], A[i]
                p2 -= 1    # 然后p2指针向前移一位
            elif A[i] == 1:  # 遇到1则i继续向前遍历
                i += 1
            elif A[i] == 0:  # 遇到0则把0和p0指向的数交换
                A[i], A[p0] = A[p0], A[i]
                p0 += 1      # 然后p0指针向后移一位
                # 注意这里i也要加1,因为如果前面有2早就被换到后面p2指针所指的地方去了，因此只可能和1换位置或者本身原地在换
                i += 1       # 然后i继续向前遍历，
        return A

if __name__ == '__main__':
    s = Solution()
    print s.sortColors([])
    print s.sortColors([2, 2, 0, 2, 1])
    print s.sortColors([2,1,1,0])
    print s.sortColors([1, 0, 0, 1])

################################################################################################
# 这道题要求只能扫描一遍并且要in place，采用两个指针交换A中的元素来实现。p0指向0该放的位置，p2
# 指向2该放的位置，i遍历整个数组，遇到0则把0和p0指向的数交换；遇到2则把2和p2指向的数交换；遇到1则
# 继续向后遍历。注意p0, p2，i三个指针的变动规律。
#