# coding=utf8


class Solution(object):
    def increasingTriplet(self, nums):
        a = b = None
        for n in nums:
            if a is None or a >= n:
                a = n
            elif b is None or b >= n:
                b = n
            else:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [5, 4, 3, 2, 1]
    print s.increasingTriplet(nums)
