# coding=utf8

__author__ = 'smilezjw'


def removeDuplicates(A):
    if len(A) == 0:
        return 0
    j = 1
    for i in xrange(1, len(A)):
        if A[i] != A[i - 1]:     # 判断连续两个整数是否相同
            A[j] = A[i]          # 使用两个指针，j记录上一个去重的整数的下一个位置
            j += 1
    #return (j, A)
    return j

if __name__ == '__main__':
    print removeDuplicates([])
    print removeDuplicates([1,1])
    print removeDuplicates([1,1,2])
    print removeDuplicates([1,1,2,3,3,5,5])

########################################################################################
# 这道题比较简单，唯一需要动脑筋的是不能另外分配数组，那只能对原有的数组进行修改。
# 由于数组已经排好序，因此只要判断连续两个整数是否相同，使用两个指针，
# i从0开始遍历整个数组，j从0开始记录每一个不重复的整数，即对A[:j]重新赋值为已经去重后的
# 整数。
# LeetCode还会判断A[:j]是否为去重后的数组，因此不能仅仅用一个变量对不重复的元素进行计数。