# coding=utf-8

__author__ = 'smilezjw'

import numpy as np

def findMedianSortedArrays(A, B):
    # leetcode不能import任何库啊啊啊= =
    # a = np.array(A, dtype=int)
    # b = np.array(B, dtype=int)
    # arr = np.union1d(a, b)
    # return np.median(arr)

# 需要判断奇数偶数的情况
    lenA, lenB = len(A), len(B)
    if (lenA + lenB) % 2 == 1:
        return get_kth_smallest_number(A, B, (lenA + lenB) / 2 + 1)
    else:
        return (get_kth_smallest_number(A, B, (lenA + lenB) / 2) + \
                get_kth_smallest_number(A, B, (lenA + lenB) / 2 + 1)) * 0.5

# 转换为求第k小个元素， 则中位数为求第 (len(A) + len(B)) / 2 + 1 个元素
# 分别对A和B求出第 k/2 位置的元素，如果A[k/2] <= B［k/2]，则A[:k/2]这些元素都不可能是第k小个元素，
# 因此去除这部分元素。例如k=6, A3 <= B3, 则最多有2个元素小于A1, 最多有3个元素小于A2, 最多有4个元素小于A3,
# 至少有5个元素小于B3，因此A1 A2 A3不可能是第6小元素，需要去掉。
# 这里采用了分治法的思想。
def get_kth_smallest_number(A, B, k):
    lenA, lenB = len(A), len(B)
    if lenA == 0 and lenB == 0:
        return 0
    elif lenA == 0 and lenB != 0:
        return B[k-1]
    elif lenB == 0 and lenA != 0:
        return A[k-1]
    elif k == 1:
        return min(A[0], B[0])
    else:
        pa = min(k/2, lenA)    # 递归，停止条件为 k = 1 或者 A 的长度为0 或者B的长度为0
        pb = min(k/2, lenB)
        if A[pa - 1] <= B[pb - 1]:
            return get_kth_smallest_number(A[pa:], B, k - pa)
        else:
            return get_kth_smallest_number(A, B[pb:], k - pb)

if __name__ == '__main__':
   print  findMedianSortedArrays([2,4,6,8,10], [1,3,5,9])


#####################################################################################3
# 这道题采用了分治法的思想，将原题目转换为求第k小个元素。
#