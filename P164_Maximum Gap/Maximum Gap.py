# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # O(nlogn)
    def maximumGap(self, num):
        length = len(num)
        if length < 2:
            return 0
        num.sort()
        maxGap = 0
        for i in xrange(length-1):
            maxGap = max(maxGap, num[i+1] - num[i])
        return maxGap

    # 桶排序
    # 列表中有N个元素，最小值为minimum，最大值为maximum，
    # 那么最大差值不会小于(maximum - minimum - 1) / (N - 1),相当于最大值与最小值的分到N-1个间隔中
    # 每个桶的大小为range = ceiling((maximum - minimum) / (N - 1))
    # 桶的个数最多为len = (B - A) / range + 1
    # 对于数组中的任意整数k，可以通过loc = (k - minimum) / range找到桶的位置
    # 记录每一个桶中的最大值和最小值
    # 由于同一个桶中的元素之间的差值最大不超过range - 1,
    # 因此最大差值从两个相邻的非空的桶中计算
    def maximumGap_Bucket(self, num):
        N = len(num)
        if N < 2:
            return 0
        minimum = min(num)
        maximum = max(num)
        bucketRange = max(1,  (maximum - minimum - 1) / (N - 1) + 1)
        bucketLen = (maximum - minimum) / bucketRange + 1
        buckets = [None] * bucketLen
        for k in num:
            loc = (k - minimum) / bucketRange
            bucket = buckets[loc]
            if bucket is None:
                bucket = [k, k]
                buckets[loc] = bucket
            else:
                bucket[0] = min(bucket[0], k)
                bucket[1] = max(bucket[1], k)
        maxGap = 0
        x = 0
        while x < bucketLen:
            if buckets[x] is None:
                continue
            y = x + 1
            while y < bucketLen and buckets[y] is None:
                y += 1
            if y < bucketLen:
                maxGap = max(maxGap, buckets[y][0] - buckets[x][1])
            x = y
        return maxGap

if __name__ == '__main__':
    s = Solution()
    num = [12, 6, 3, 7]
    num2 = [1,1,1,1,1,5,5,5,5,5]
    num3 = [1,10000000]
    # print s.maximumGap(num)
    # print s.maximumGap_Bucket(num2)
    print s.maximumGap_Bucket(num3)

#######################################################################################
# 给定一个未排序的数组，找出其排序后的序列中两个相邻元素之间的最大差值，能够在线性时间
# 和线性空间复杂度内完成。两种方法求解：
# 1.直接对该数组排序，然后求得排序后相邻两个元素之间的最大差值。时间复杂度为O(nlogn)。
# 2.桶排序，需要注意每个桶的大小，已经最多桶的个数，记录每个桶中的最大元素和最小元素，
# 注意最大差值是从相邻的两个非空的桶之间计算得出。
#