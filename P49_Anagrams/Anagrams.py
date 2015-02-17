# coding=utf8

__author__ = 'smilezjw'


class Solution():
    def anagrams(self, strs):
        hashTable = {}  # 构建hash表，key为按字母顺序排序的字符串，值为相应的字符串列表
        res = []
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in hashTable:
                hashTable[sortedWord] = [word]
            else:
                hashTable[sortedWord].append(word)
        for i in hashTable:
            if len(hashTable[i]) > 1:  # 返回所有存在anagrams的字符串
                res += hashTable[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print s.anagrams(['', ' '])
    print s.anagrams(['abc', 'bac', 'cab', 'car'])

#############################################################################################
# anagrams的意思是：'abc', 'bac', 'cab' 等由相同字母构成的字符串（即同一字符串不同字母排序）。
# 这里构建hash表，键为按照字母排序得到的字符串，值为对应的由这些字母组成的字符串。
# 最后找出由两个及以上anagrams的字符串即可。
#