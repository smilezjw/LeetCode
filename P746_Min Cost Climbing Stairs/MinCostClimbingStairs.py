# coding=utf8

class Solution(object):
    def minCostClimbingStairs(self, cost):
        step1 = step2 = 0
        for c in cost:
            step1, step2 = min(step1, step2) + c, step1
        return min(step1, step2)

if __name__ == '__main__':
    solution = Solution()
    cost0 = [10, 15, 20]
    print solution.minCostClimbingStairs(cost0)

    cost1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print solution.minCostClimbingStairs(cost1)
