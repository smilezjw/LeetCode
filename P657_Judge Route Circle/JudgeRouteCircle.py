# coding=utf8

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        upDown = 0
        leftRight = 0
        for move in moves:
            if move == 'U':
                upDown += 1
            elif move == 'D':
                upDown -= 1
            elif move == 'L':
                leftRight -= 1
            else:
                leftRight += 1
        return upDown == 0 and leftRight == 0

if __name__ == '__main__':
    solution = Solution()
    print solution.judgeCircle('UD')
    print solution.judgeCircle('LL')