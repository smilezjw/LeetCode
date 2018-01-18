# coding=utf8

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        num = len(points)
        res = 0
        for i in range(num):
            dist = {}
            for j in range(num):
                distance = self.calculateDistance(points[i], points[j])
                if distance not in dist:
                    dist[distance] = [j]
                else:
                    dist[distance].append(j)
            for distance in dist:
                cnt = len(dist[distance])
                if cnt < 2:
                    continue
                else:
                    res += cnt * (cnt - 1)
        return res


    def calculateDistance(self, pointA, pointB):
        x1, y1 = pointA
        x2, y2 = pointB
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

if __name__ == '__main__':
    solution = Solution()
    points0 = [[0,0],[1,0],[2,0]]
    print(solution.numberOfBoomerangs(points0))
