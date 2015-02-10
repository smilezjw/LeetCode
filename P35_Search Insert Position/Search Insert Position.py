# coding=utf8

__author__ = 'smilezjw'


def searchInsertPos(A, target):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) / 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left  # 注意这里是返回left的位置，即为target插入的位置，或者是right+1

if __name__ == '__main__':
    print searchInsertPos([1, 3, 5, 6], 5)
    print searchInsertPos([1, 3, 5, 6], 7)
    print searchInsertPos([1, 3, 5, 6], 0)
    print searchInsertPos([1, 3], 2)

##############################################################################################
# 又是一道binary search的题目，需要注意的是最后如果原来列表里面没有target，则最后返回left的
# 位置即为target插入的位置（或者是right+1）。
#