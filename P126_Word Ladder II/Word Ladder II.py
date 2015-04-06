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
        # 从end到start从后往前构建路径
        def buildpath(path, word):
            if len(prevMap[word]) > 0:
                for n in prevMap[word]:
                    buildpath(path+[word], n)
            elif len(prevMap[word]) == 0:
                currPath = path[:]  # 注意这里不能修改path
                currPath.append(word)
                currPath.reverse()  # 因为是从后往前所以这里要reverse()
                result.append(currPath)
            return

        result = []
        prevMap = {}  # 前驱单词表，用字典形式表示，键为某个单词，值为某个单词通过修改一个字母得到该单词
        dict.add(start)  # 把start和end都添加到集合中
        dict.add(end)
        length = len(start)
        for i in dict:
            prevMap[i] = []  # 初始化前驱单词表
        candidates = [set(), set()]
        current = 0
        previous = 1
        candidates[current].add(start)  # current记录的是当前遍历的单词， previous记录的是前驱单词
        while True:
            current, previous = previous, current  # 这里呼唤就是一个技巧
            for i in candidates[previous]:  # 在dict中将当前遍历的单词删除
                dict.remove(i)
            candidates[current].clear()     # 将上一层前驱单词清空
            for word in candidates[previous]:
                for i in xrange(length):
                    part1 = word[:i]
                    part2 = word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            nextword = part1 + j + part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)  # 这里就是在记录当前这一层得到的单词
            if len(candidates[current]) == 0:
                return result
            if end in candidates[current]:
                break
        buildpath([], end)
        return result

if __name__ == '__main__':
    s = Solution()
    print s.findLadders("red", "tax", set(["ted","tex","red","tax","tad","den","rex","pee"]))
    print s.findLadders('hot', 'dog', set(['hot', 'dog']))
    print s.findLadders('a', 'c', set(['a', 'b', 'c']))
    print s.findLadders(start='hot', end='dog', dict=set(["hot","dog","dot"]))
    print s.findLadders(start='hit', end='cog', dict=set(["hot","dot","dog","lot","log"]))

########################################################################################
# 这道题想了两次才想明白，需要注意以下几点：
# 1. LeetCode OJ给定例子中start和end是不在dict中的，但是测试用例中start和end貌似是包括在
# dict中的，因此程序里通过dict.add(start); dict.add(end);避免这种问题，因为dict是无序不
# 重合集合。
# 2. 使用前驱单词表prevMap，字典类型记录单词及其前驱单词。然后根据前驱单词表从后往前构建
# end到start的路径，最后将该路径reverse()即可得到一个解。
# 3.使用两个set()， candidate[previous]存储的是前一层的单词（前驱单词），将前驱单词在dict
# 中删除避免死循环，再将candidate[current]清空；然后根据candidate[previous]中的单词寻找
# 下一层单词记录在candidate[current]中，下一次循环开始前，上一次循环中的candidate[current]
# 就变成了candidate[previous]。如此循环，直到candidate[current]中出现了end时，则最短的路径
# 已经找到了。
#