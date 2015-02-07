# coding=utf8

__author__ = 'smilezjw'


def removeElement(A, elem):
    j = 0
    for i in xrange(len(A)):
        if A[i] != elem:
            A[j] = A[i]  # 使用两个指针，A[:j]记录保留的元素
            j += 1
    #print A
    return j

if __name__ == '__main__':
    print removeElement([1,2,2,3,2,5], 2)

#############################################################################################
# 这道题和26题基本是一样的思路啊，26题是在有序列表中remove重复元素；这题是在列表中remove指定
# 元素。都采用两个指针，i遍历列表，j则从0开始A[j]记录保留下来的元素。
#