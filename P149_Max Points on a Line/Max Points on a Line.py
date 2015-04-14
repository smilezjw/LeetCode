# coding=utf8

__author__ = 'smilezjw'


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        length = len(points)
        if length <= 2:  # 两点能够确定一条直线
            return length
        res = -1
        for p in xrange(length):
            # 注意当斜率为无穷大，对于每一个点，都重新设置hash表，因为如果斜率相同，截距不同的直线就不是同一条直线
            slope = {'inf': 0}
            samePoints = 1      # 如果有两个一样的点，要算两次的
            for q in xrange(length):
                if p == q:
                    continue
                if points[p].y != points[q].y:
                    k = (points[p].x - points[q].x) * 1.0 / (points[p].y - points[q].y)  # 计算斜率
                    if k in slope:
                        slope[k] += 1
                    else:
                        slope[k] = 1
                # 当两个点在一条平行于x州的直线上时，此时斜率为正无穷
                elif points[p].y == points[q].y and points[p].x != points[q].x:
                    slope['inf'] += 1
                # 记录一样的点有多少个
                else:
                    samePoints += 1
            res = max(res, max(slope.values()) + samePoints)
        return res

if __name__ == '__main__':
    s = Solution()
    p1 = Point(0, 0)
    pp = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(0, 1)
    p4 = Point(1, 1)
    p5 = Point(2, 2)
    points = [p1, p2, p3, p4, p5]
    points2 = [p1, pp]
    print s.maxPoints(points)

##########################################################################################
# 对于每一个点，都计算该点和其他点所在的直线的斜率，如果斜率相同，那么这些点在一条直线上。
# 注意对每个点都要重新维护一张斜率的hash表，slope = {k:pointsNum},因为虽然有两条直线斜率相
# 同但是截距不同，只能是两条平行的直线。另外当斜率为正无穷时要另外判断，避免计算斜率报错。
# 注意两个相同的点要算两次，因此用变量samePoints记录和当前的点相同的点的个数。
#