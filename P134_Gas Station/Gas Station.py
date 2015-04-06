# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 这种解法报错Runtime error
    def canCompleteCircuit_DFS(self, gas, cost):
        length = len(gas)
        gas += gas
        cost += cost
        for i in xrange(length):
            if self.complete(i, i, length, gas, cost, 0):
                return i
        return -1

    def complete(self, start, end, length, gas, cost, remain):
        if start - end == length:
            return True
        if remain + gas[start] >= cost[start]:
            self.complete(start+1, end, length, gas, cost, remain + gas[start] - cost[start])
            return True
        else:
            return False

    # 这种做法好简单！
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):  # 如果所有可加的油都不够开完整条环路，返回-1
            return -1
        length = len(gas)
        remain = 0  # 假设每个加油站都去加油，然后每开一站后剩下的总共的油量
        stationIndex = 0
        for i in xrange(length):
            # 如果剩下的油量加上这一站新加的油量都不够开往下一站，那么重新将下一站设置为起点
            if gas[i] + remain < cost[i]:
                stationIndex = i + 1
                diff = 0
            # 否则继续累加剩余的油量
            else:
                remain += gas[i] - cost[i]
        return stationIndex

if __name__ == '__main__':
    s = Solution()
    print s.canCompleteCircuit([1, 2], [2, 1])
    print s.canCompleteCircuit([1,2,3,3], [2,1,5,1])

########################################################################################
# 首先判断所有的加油站可以加的油量是否满足整条路上要消耗的油量，如果不够则直接返回-1。
# 如果够的话，可以一边扫描gas和cost列表，判断当前剩余的油量加上第i站新加的油量是否够开往
# 下一站，如果够的话则继续累加剩余油量；如果不够则重新将下一站设置为起点站。由于整体已经
# 判断是够开完整条路径的，因此只要一遍扫描找到起始点，那么循环这条路径后面的站点油量肯定
# 是够的。
# 需要注意的是这里stationIndex是从0开始计算的。