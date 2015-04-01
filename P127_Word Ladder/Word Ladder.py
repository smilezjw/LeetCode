# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def ladderLength(self, start, end, dict):
    #     Solution.minLength = 2 ** 31 - 1
    #     self.dfs(start, end, dict, 0)
    #     if Solution.minLength == 2 ** 31 - 1:
    #         return 0
    #     else:
    #         return Solution.minLength + 2
    #
    # def dfs(self, start, end, dict, length):
    #     for i in xrange(len(dict)):
    #         startDiff = 0
    #         endDiff = 0
    #         for j in xrange(len(dict[0])):
    #             if start[j] != dict[i][j]:
    #                 startDiff += 1
    #             if end[j] != dict[i][j]:
    #                 endDiff += 1
    #         if endDiff == 1 and length < Solution.minLength:
    #             Solution.minLength = length
    #         elif startDiff == 1:
    #             if start in dict:
    #                 curr = dict[:]
    #                 curr.remove(start)
    #                 self.dfs(dict[i], end, curr, length+1)
    #             else:
    #                 self.dfs(dict[i], end, dict, length+1)

    def ladderLength(self, start, end, dict):
        dict.add(end)  # 注意这里dict是集合类型，是无序不重复元素集
        q = []
        q.append((start, 1))
        while q:
            curr = q.pop(0)
            currWord = curr[0]
            currLen = curr[1]
            if currWord == end:  # 最先找到的路径，就是最短路径
                return currLen
            for i in xrange(len(start)):
                part1 = currWord[:i]
                part2 = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':  # 时间复杂度为O(26*L)
                    if currWord[i] != j:
                        nextWord = part1 + j +part2
                        if nextWord in dict:
                            q.append((nextWord, currLen + 1))
                            dict.remove(nextWord)
        return 0

if __name__ == '__main__':
    s = Solution()
    print s.ladderLength('a', 'c', set(['a', 'b', 'c']))
    print s.ladderLength(start='hit', end='cog', dict=set(["hot","dot","dog","lot","log"]))

#########################################################################################
# 注意这里的dict是集合set类型，检查一个单词是否在集合中时间复杂度为O(1)。设单词长度为L，
# dict里面有N个单词，每次扫一遍dict判断每个单词是否与前一个单词只差一个字母是时间复杂度为
# O(N*L),但是每次变换当前单词的一个字母，查看变换的单词是否在集合中时间复杂度为O(26*L)。
# 集合中每个单词只能使用一次，不然会无限循环下去，所以用过就删除掉。
#
