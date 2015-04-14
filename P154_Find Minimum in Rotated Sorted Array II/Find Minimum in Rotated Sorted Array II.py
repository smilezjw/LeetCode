# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def findMin(self, num):
        left = 0
        right = len(num) - 1
        # 旋转列表一定满足num[left] >= num[right], 否则left就是指向最小值
        while left < right and num[left] >= num[right]:
            mid = (left + right) / 2
            if num[mid] > num[left]:  # 旋转的部分在右边
                left = mid + 1        # 因为mid指向的值已经比left指向的值大了，所以mid不可能指向最小值，因此left直接指向mid+1
            elif num[mid] < num[right]:  # 旋转的部分在左边
                right = mid           # 因为mid指向的值可能是最小值，因此right指向mid
            else:
                left += 1  # 由于出现重复的值，无法判断旋转的部分在左边还是右边，因此left+1
        return num[left]

if __name__ == '__main__':
    s = Solution()
    num1 = [4, 5, 6, 7, 0, 0, 1, 2]
    num2 = [3, 3, 1, 3]
    num3 = [3, 1, 1]
    num4 = [10, 1, 10, 10, 10]
    print s.findMin(num1)

##########################################################################################
# 由于出现重复值的情况，可能无法判断旋转的部分在mid左边还是右边，此时则left+1，反正这时候
# 即使指向最小值，之后也可以判断出来的。
#