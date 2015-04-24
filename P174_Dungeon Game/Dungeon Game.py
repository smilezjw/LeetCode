# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)     # 二维数组的行数
        n = len(dungeon[0])  # 二维数组的列数
        # 开辟一个新的二维数组dp[i][j]保证骑士在进入房间（i,j）之前，探索地牢其余房间能够存活下来的最小生命值
        dp = [[0] * n for i in xrange(m)]
        # dp[-1][-1]表示骑士探索最后一个地牢之前能够存活下来的最小的生命值
        # 如果dungeon[-1][-1] >= 0, 则骑士至少保持1个生命值；否则骑士需要保持-dungeon[i][j] + 1
        dp[-1][-1] = max(0, -dungeon[-1][-1]) + 1

        # 初始化最后一列
        for j in xrange(n-2, -1, -1):
            dp[-1][j] = max(dp[-1][j+1] - dungeon[-1][j], 1)
        # 初始化最后一行
        for i in xrange(m-2, -1, -1):
            dp[i][-1] = max(dp[i+1][-1] - dungeon[i][-1], 1)
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                # 骑士离开房间时的最小生命值，取决于探索两条路径(i+1, j)和(i, j+1)之前需要的最小生命值
                # dp[i][j]表示其实进入房间(i,j)之前需要的最小生命值，则由离开这个房间时的最小生命值和在这个房间内的情况所决定
                # 如果dungeon[i][j] == 0,则骑士进入这个房间和离开时生命值保持一致，dp[i][j] = min(dp[i+1][j], dp[i][j+1])
                # 如果dungeon[i][j] > 0, 则骑士离开这个房间时生命值大于进入时， 因此dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j],
                # 但是这种情况可能会使得骑士进入房间之前生命值已经小于等于0，因此限制dp[i][j]至少为1
                # 如果如果dungeon[i][j] < 0, 则骑士离开这个房间时生命值小于进入时，因此dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j],
                # 总结上述3中情况，得到状态转移方程
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        # 最后返回dp[0][0]就是骑士进入地牢之前初始时候的生命值最小值
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    dungeon = [[-2, -3, 3],
               [-5, -10, 1],
               [10, 30, -5]]
    dungeon2 = [[100]]
    print s.calculateMinimumHP(dungeon)
    print s.calculateMinimumHP(dungeon2)

#######################################################################################
# 一开始以为和maximum/minimum path sum问题很相似，但是具有全局最大生命值的路径并不一定
# 是最小的初始的生命值，题目中有限制条件任意时刻生命值不能小于等于0。
# 用“表格填充”动态规划算法求解。建立一个新的二维数组，dp[i][j]表示骑士在进入房间(i,j)
# 之前，探索其他地牢能够存活下来的最小的生命值。那么dp[0][0]就是最终的答案了，骑士在进入
# (0,0)房间前初始的最小生命值。
#