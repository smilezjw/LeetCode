# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def removeDuplicates(self, A):
    #     if len(A) == 0:
    #         return 0
    #     j = 1  # j位置用来记录结果
    #     count = 1  # 对当前元素计数
    #     for i in xrange(1, len(A)):
    #         if A[i] != A[i-1]:  # 如果当前元素和上一个元素不相等，那么count=1表示出现第一次
    #             A[j] = A[i]     # 并且将A[i]放到j位置上
    #             j += 1
    #             count = 1
    #         elif A[i] == A[i-1] and count == 1:  # 如果当前元素和上一个元素相同，但是count=1,说明这是第二次出现
    #             count += 1
    #             A[j] = A[i]     # 将A[i]放到j位置上，说明A[i]这个元素出现两次，但是最多出现两次
    #             j += 1
    #     return j    # 返回的j就是最多出现两次的所有元素的出现的次数

    def removeDuplicates(self, A):
        if len(A) <= 2:
            return 2
        prev = 1
        curr = 2
        while curr < len(A):
            # 如果curr和prev和prev-1指向的三个值都相等，那么curr继续向后遍历
            if A[curr] == A[prev] and A[prev] == A[prev - 1]:
                curr += 1
            else:
                # 如果curr和prev不相等，那么prev+1的位置记录curr指向的值（说明A[curr]是第一次出现），然后curr继续向后遍历
                # 或者prev和prev-1不相等，（A[curr] == A[prev] 或者 A[curr] != A[prev],符合最多出现两次的规则）那么prev+1的
                # 位置记录curr指向的值，然后curr继续向后遍历
                prev += 1
                A[prev] = A[curr]
                curr += 1
        return prev + 1

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,1, 2, 2, 2,2,3])

###########################################################################################
# 这道题用了两种解法。第一种方法和第26题类似的思路，引入变量count记录元素出现的次数，如果
# A[i] != A[i-1], 说明A[i]是第一次出现，在j位置记录下来；如果A[i]==A[i-1]并且count==1，说明
# 这是第二次出现，依然可以在j位置记录下来；否则i继续向后遍历。
# 第二种方法用两个指针curr和prev,如果A[curr] == A[prev] == A[prev+1],那么curr继续向后遍历；
# 否则A[prev+1] = A[curr],然后curr继续向后遍历。注意返回的时候prev+1,因为从0开始记录最多出现两次
# 的元素。
#