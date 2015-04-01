# coding=utf8

__author__ = 'smilezjw'


class Solution:
    #def findLadders(self, start, end, dict):
        # dict.add(start)
        # dict.add(end)
        # q = []
        # q.append(start)
        # prevMap = {}
        # while q:
        #     # currWord = q.pop(0)
        #     # prevMap[currWord] = []
        #     # if currWord == end:
        #     #     break
        #     temp = q[:]
        #     q = []
        #     for currWord in temp:
        #         for i in xrange(len(start)):
        #             part1 = currWord[:i]
        #             part2 = currWord[i+1:]
        #             for j in 'abcdefghijklmnopqrstuvwxyz':
        #                 if currWord[i] != j:
        #                     nextWord = part1 + j + part2
        #                     if nextWord != start and nextWord in dict:
        #                         q.append(nextWord)
        #                         if currWord in prevMap:
        #                             prevMap[currWord] += [nextWord]
        #                         else:
        #                             prevMap[currWord] = [nextWord]
        #                         #if nextWord != end:
        #         dict.remove(currWord)

        # def buildPath(path, start, end, prevMap):
        #     if start == end:
        #         Solution.res.append(path+[end])
        #     elif start in prevMap.keys() and len(prevMap[start]) > 0:
        #         for i in xrange(len(prevMap[start])):
        #             buildPath(path+[start], prevMap[start][i], end, prevMap)
        # #print prevMap
        # Solution.res = []
        # result = {}
        # buildPath([], start, end, prevMap)
        # if Solution.res == []:
        #     return Solution.res
        # for i in xrange(len(Solution.res)):
        #     length = len(Solution.res[i])
        #     if length not in result:
        #         result[length] = [Solution.res[i]]
        #     else:
        #         result[length] += [Solution.res[i]]
        # return result[min(result.keys())]


    def findLadders(self, start, end, dict):
        prevMap = {}
        result = []
        dict.add(start)
        dict.add(end)
        wordLength = len(start)
        previous = set()
        current = set()
        current.add(start)
        while True:
            previous = current
            current = set()
            for word in previous:
                for k in xrange(wordLength):
                    part1 = word[:k]
                    part2 = word[k+1:]
                    for j in 'abcdefghijklmnopqrtuvwxyz':
                        if word[k] != j:
                            nextWord = part1 + j + part2
                            if nextWord in dict and nextWord not in previous:
                                current.add(nextWord)
                                if nextWord not in prevMap:
                                    prevMap[nextWord] = [word]
                                else:
                                    prevMap[nextWord] += [word]
                dict.remove(word)

            if end in current:
                break
            if len(current) == 0:
                return result

        print prevMap

        def buildPath(path, start, end, prevMap):
            if start == end:
                Solution.res.append(path+[end])
            elif start in prevMap.keys() and len(prevMap[start]) > 0:
                for i in xrange(len(prevMap[start])):
                    buildPath(path+[start], prevMap[start][i], end, prevMap)

        Solution.res = []
        buildPath([], start, end, prevMap)
        return Solution.res



if __name__ == '__main__':
    s = Solution()
    print s.findLadders("red", "tax", set(["ted","tex","red","tax","tad","den","rex","pee"]))
    print s.findLadders('hot', 'dog', set(['hot', 'dog']))
    print s.findLadders('a', 'c', set(['a', 'b', 'c']))
    print s.findLadders(start='hot', end='dog', dict=set(["hot","dog","dot"]))
    print s.findLadders(start='hit', end='cog', dict=set(["hot","dot","dog","lot","log"]))