# coding=utf8

__author__ = 'smilezjw'


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        #将需要insert and merge的区间直接添加到列表中，然后完全按照上一题的思路继续merge
        intervals += [newInterval]
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in xrange(1, len(intervals)):
            j = len(res) - 1
            if intervals[i].start >= res[j].start and intervals[i].start <= res[j].end:
                res[j].end = max(intervals[i].end, res[j].end)
            else:
                res.append(intervals[i])
        return res

##########################################################################################
# 这道题先把需要插入到区间直接插入到列表中，然后完全按照上一题的思路解决。
#