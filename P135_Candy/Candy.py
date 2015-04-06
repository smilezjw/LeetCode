# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def candy(self, ratings):
        length = len(ratings)
        candy = [1 for i in xrange(length)]  # 初始化， 每个孩子至少要有一颗糖
        # 正向扫描，如果是递增序列，则糖果数也递增
        for i in xrange(1, length):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        # 反向扫描，如果是递增序列，并且更改后的糖果数不符合递增的情况，则修改糖果数分配为递增序列
        for i in xrange(length-1, 0, -1):
            if ratings[i] < ratings[i-1] and candy[i] >= candy[i-1]:
                candy[i-1] = candy[i] + 1
        return sum(candy)

if __name__ == '__main__':
    s = Solution()
    print s.candy([0])
    print s.candy([1, 2, 2])
    print s.candy([4, 2, 3, 4, 1])

#######################################################################################
# 这道题不能用排序，因为需要考虑每个元素和它相邻两个元素之间的大小关系。
# 首先正向扫描列表，如果ratings是递增序列，一开始初始化糖果分配序列肯定不是递增的，则
# 使得分配糖果数也为递增序列；
# 然后反向扫描列表，如果ratings是递增序列，而分配后的糖果数不符合递增的情况，则修改分配
# 糖果数也为递增序列。
#