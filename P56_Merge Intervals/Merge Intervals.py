# coding=utf8

__author__ = 'smilezjw'


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# class Solution:    # 这种做法会超时
#     def merge(self, intervals):
#         if len(intervals) <= 1:
#             return intervals
#         res = [intervals[0]]
#         for i in intervals[1:]:
#             for j in res:
#                 if i.start <= j.start and i.end >= j.end:
#                     j.start = i.start
#                     j.end = i.end
#                 elif i.start <= j.start and i.end > j.start and i.end < j.end:
#                     j.start = i.start
#                 elif i.start > j.start and i.start < j.end and i.end >= j.end:
#                     j.end = i.end
#                 elif i.start > j.end or i.end < j.start:
#                     res.append(i)
#         return res


class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        # 这一步按照每个Interval的start从小到大排序很重要
        intervals.sort(key=lambda x: x.start)
        # 因为已经排好序了，所以res里面保存的最后一个start都比intervals下面一个start要小，
        # 直接判断下一个start是否处于res最后一个区间内，如果是的则判断end大小进行合并，
        # 否则不在区间内，那么直接添加到res中即可
        res = [intervals[0]]
        for i in xrange(1, len(intervals)):
            j = len(res) - 1
            if intervals[i].start > res[j].start and intervals[i].start <= res[j].end:
                res[j].end = max(intervals[i].end, res[j].end)
            else:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    s = Solution()
    intv = Interval()
    intv.start = 1
    intv.end = 4
    intervals = [intv, intv]
    print s.merge(intervals)

##########################################################################################
# 如果直接判断的话对于大数据集会超时；因此需要先对每个Interval的start按从小到大顺序进行排
# 序，然后判断下一个间隔的start是否处于上一个间隔范围内，是的话则判断end的范围进行合并；不是
# 则直接添加到结果列表中。
#