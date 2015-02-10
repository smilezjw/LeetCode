# coding=utf8

__author__ = 'smilezjw'

# 哈哈，这么简单的方法直接accept了好么，只要43ms哦！大家为什么非要费劲脑细胞去想如何用二分查找呢，唉= =
# def search(A, target):
#     if target in A:
#         return A.index(target)
#     else:
#         return -1

def search(A, target):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) / 2
        if A[mid] == target:
            return mid
        if A[left] < A[mid]:  # 旋转的部分在mid右边
            if A[left] <= target < A[mid]:  # left到mid之间的数字是有序的
                right = mid -1
            else:
                left = mid + 1
        elif A[left] > A[mid]:  # 旋转的部分在mid左边
            if A[mid] < target <= A[right]:  # mid和right之间的数字是有序的
                left = mid + 1
            else:
                right = mid - 1
        else:  # 如果A[left] == A[mid]
            left += 1
    return -1  # 如果没找到则返回-1

if __name__ == '__main__':
    print search([2,3,4,5,6,0,1], 6)

###############################################################################################
# 这道题一开始没看明白题目意思，直接用index做竟然也通过了，然后一看大家的解题思路才知道这道题
# 是想考binary search。主要还是要判断旋转的部分是在mid坐边还是右边，然后再判断target是在mid左边
# 还是右边，主要边界条件的判断，如A[left] == A[mid]。
#