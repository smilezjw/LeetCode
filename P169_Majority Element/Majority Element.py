# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # 127ms
    def majorityElement_Sorting(self, num):
        num.sort()
        return num[len(num) / 2]

    # 192ms
    def majorityElement_HashTable(self, num):
        hashTable = {}
        for n in num:
            if n in hashTable:
                hashTable[n] += 1
            else:
                hashTable[n] = 1
        return sorted(hashTable.items(),key=lambda x:x[1], reverse=True)[0][0]

    # 128ms
    def majorityElement_Voting(self, num):
        count = 0
        for n in num:
            if count == 0:
                candidate = n
                count += 1
            elif n == candidate:
                count += 1
            else:
                count -= 1
        return candidate

if __name__ == '__main__':
    s = Solution()
    num1 = [1,1,1,2,3]
    print s.majorityElement_Sorting(num1)
    print s.majorityElement_HashTable(num1)
    print s.majorityElement_Voting(num1)

##############################################################################################
# 这道题比较简单，要求数组中的众数，但是可以用多种方法求解，官方就给出了7种方法：
# 1.暴力搜索O(n^2)时间复杂度：两层循环，对每一个元素判断是否为众数。
# 2.哈希表O(n)时间复杂度，O(n)空间复杂度：用字典结构记录每一个元素在数组中的个数，然后找到个数
#   最多且超过一半数量的元素。
# 3.先排序O(nlogn)时间复杂度：先对数据进行排序，由于众数数量超过len(num)/2，因此直接返回
# num[len(num)/2]该元素就是众数。
# 4.随机算法平均时间复杂度O(n),最坏时间复杂度无穷大：从数组中随机选取一个元素计算出现的次数，
# 判断是否为众数。如果不是就重复随机抽取直到找到为止。
# 5. 分治法时间复杂度为O(nlogn):将数组拆成两半，分别找出前一半的众数A和后一半的众数B，如果A==B，
# 则该元素就是众数；如果A!=B，则最多只要计算这两个元素的个数即可判断众数。T(n) = T(n/2)+ 2 = O(nlogn)
# 6.Moore投票算法，时间复杂度为O(n):遍历数组，维护变量candidate为当前的候选众数，变量count为
# 计数器，如果计数器为0，则将当前元素设置为候选众数，并计数器加1；否则如果当前元素等于候选众数则
# 计数器加1；否则计数器减1。由于众数数量超过一半，因此最终得到的候选众数元素就是众数。
# 7.位操作算法O(n)时间复杂度，不太明白。
# 我这里实现了哈希表、排序以及Moore投票算法。
#