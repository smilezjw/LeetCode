# coding=utf8

__author__ = 'smilezjw'


def searchRange(A, target):
    left = 0
    right = len(A) - 1
    res = []
    while left <= right:
        mid = (left + right) / 2
        if A[mid] == target:
            for i in xrange(left, mid+1): # 在left和mid之间查找target的起始下标
                if A[i] == target:
                    res.append(i)
                    break
            for j in xrange(right, mid-1, -1): # 在right和mid之间逆向查找target的结束下标
                print j
                if A[j] == target:
                    res.append(j)
                    break
            return res
        elif A[mid] > target:
            right = mid - 1
        else:  # A[mid] < target
            left = mid + 1
    return [-1, -1]

if __name__ == '__main__':
    print searchRange([5,7,7,8,8,10], 8)
    print searchRange([1],0)

#############################################################################################
# 又是一道二分查找的题目，做完上一道对这一道题就感觉熟悉了，自己也能写出来了。
# 时间复杂度为O(log)n
