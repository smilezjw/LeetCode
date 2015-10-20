# coding=utf8

__author__ = 'smilezjw'

import heapq

class MedianFinder(object):
    def __init__(self):
        # 用大顶堆和小顶堆来实现
        # heapq中实现的是小顶堆，大顶堆则存数据时存入相反数
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        # 如果当前数据量为偶数，则将num存入小顶堆，但是要保证存入小顶堆的数字是大顶堆中最大的
        # 这样才能保证后半部分数字都要比前半部分数字大
        if len(self.minHeap) == len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        # 如果当前数据量为奇数，则将num存入大顶堆保持大顶堆和小顶堆数量相同
        # 但是要将小顶堆中最小的数字存入大顶堆中，这样才能保证前半部分的数字都要比后半部分数字小
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))

    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return self.minHeap[0]

if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(6)
    print mf.findMedian()
    mf.addNum(10)
    print mf.findMedian()
    mf.addNum(2)
    print mf.findMedian()
    mf.addNum(6)
    print mf.findMedian()
    mf.addNum(5)
    print mf.findMedian()
    mf.addNum(0)
    print mf.findMedian()
    mf.addNum(6)
    print mf.findMedian()
    mf.addNum(3)
    print mf.findMedian()
    mf.addNum(1)
    print mf.findMedian()
    mf.addNum(0)
    print mf.findMedian()
    mf.addNum(0)
    print mf.findMedian()

