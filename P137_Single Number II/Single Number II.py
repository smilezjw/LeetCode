# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def singleNumber(self, A):
        if len(A) == 1:  # 如果只有一个元素，那么直接返回这个元素
            return A[0]
        A.sort()         # 排序是为了使得所有相等的元素能够相邻
        i = 1            # i保持在连续三个相等的元素中的第二个元素的位置
        while i < len(A):
            if A[i] == A[i-1]:  # 连续三个相等的元素
                i += 3
            else:
                return A[i-1]    # 找到单个出现的元素
        return A[-1]   # 因为肯定会存在单个出现的元素，因此如果前面列表没有找到的话，那肯定是最后一个元素了


if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1])
    print s.singleNumber([2,2,3,2])
    print s.singleNumber([1,1,1,2,2,2,3])
    print s.singleNumber([1,1,1,2,3,3,3])

#############################################################################################
# 这道题我没有用位操作，网上位操作的思路实在是没看太明白，想来也没太大意思，能够掌握上一题中
# 的位操作就挺好的。于是就有了自己的解法，简单易懂，Accept 71ms。
#