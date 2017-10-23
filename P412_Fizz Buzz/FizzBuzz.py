# coding=utf8

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # res = []
        # fizzBuzz = 'FizzBuzz'
        # fizz = 'Fizz'
        # buzz = 'Buzz'
        # for i in xrange(1, n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         res.append(fizzBuzz)
        #     elif i % 3 == 0:
        #         res.append(fizz)
        #     elif i % 5 == 0:
        #         res.append(buzz)
        #     else:
        #         res.append(str(i))
        # return res


        # faster with two points instead of %(mod)
        res = []
        fizz = 1
        buzz = 1
        fizzBuzzStr = 'FizzBuzz'
        fizzStr = 'Fizz'
        buzzStr = 'Buzz'
        for i in xrange(1, n+1):
            if fizz == 3 and buzz == 5:
                res.append(fizzBuzzStr)
                fizz = 1
                buzz = 1
            elif fizz == 3:
                res.append(fizzStr)
                fizz = 1
                buzz += 1
            elif buzz == 5:
                res.append(buzzStr)
                buzz = 1
                fizz += 1
            else:
                res.append(str(i))
                fizz += 1
                buzz += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print solution.fizzBuzz(15)
    print 2**32