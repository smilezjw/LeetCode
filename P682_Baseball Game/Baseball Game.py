# coding=utf8

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        if len(ops) == 0:
            return 0
        scores = []
        for o in ops:
            if o == "C":
                scores.pop()
            elif o == "D":
                scores.append(scores[-1] * 2)
            elif o == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(o))
        return sum(scores)


if __name__ == '__main__':
    sol = Solution()
    print sol.calPoints(["5", "2", "C", "D", "+"])
    print sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
