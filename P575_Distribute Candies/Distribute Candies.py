# coding=utf8

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candySet = set(candies)
        return min(len(candySet), len(candies)/2)

if __name__ == '__main__':
    solution = Solution()
    print solution.distributeCandies([1, 1, 2, 2, 3, 3])
    print solution.distributeCandies([1,1,2,3])

    print 'hello'[::-1]
