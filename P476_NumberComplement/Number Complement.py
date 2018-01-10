# coding=utf8

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i <<= 1
        return num ^ (i-1)

if __name__ == '__main__':
    solution = Solution()
    num = 5
    print(solution.findComplement(num))