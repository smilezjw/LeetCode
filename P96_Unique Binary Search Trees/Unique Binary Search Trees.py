# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def numTrees(self, n):
        # 如果结点个数为0，则就是一个NULL结点，所以dp[0]=1
        dp = [0 for i in xrange(n+1)]
        dp[0] = 1
        # dp[1] = 1  # 枚举就可以得出一个结点和两个结点的解
        # dp[2] = 2
        for nodeNum in xrange(1, n+1):  # 依次算出一个结点一直到n个结点的解的个数
            # 结点个数为nodenum时，根结点下的左子树个数从0到nodenum-1（一个根结点）
            # 右子树个数则为nodenum - 1 - leftnum
            for leftNum in xrange(nodeNum):
                dp[nodeNum] += dp[leftNum] * dp[nodeNum-1-leftNum]  # 做乘法排列组合
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print s.numTrees(1)
    print s.numTrees(3)

#####################################################################################
# 解题技巧：一般来说求数量，首先想到是否可以用动态规划求解。
# 这道题求状态转移方程，n=0时为空树，dp[0]=1；
# n=1时显然也是1，dp[1]=1；
# 对于n>=2，一旦确定根结点是x，那么左子树只能由1,2，...，x-1构成，
# 右子树由x+1,x+2,...,n构成，然后做乘法进行排列组合，得到从2到n个结点的解的个数。
#