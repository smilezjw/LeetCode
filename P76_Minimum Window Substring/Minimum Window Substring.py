# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def minWindow(self, S, T):    # 这种方法会超时
    #     hashTable = [i for i in T] #表示为列表的形式
    #     temp = hashTable[:]        # 分片赋值的方式
    #     minSize = 2 ** 31 - 1
    #     res = ''
    #     begin = 0  # 记录字符串窗口的起始位置
    #     i = 0
    #     while i < len(S):
    #         if S[i] in temp:
    #             if len(temp) == len(T):
    #                 begin = i
    #             temp.remove(S[i])   # 如果是T中的字符，则在列表中删去该字符表示已经出现过了
    #             if len(temp) == 0:  # 如果列表为空，则表示所有字符串都出现过了，那么窗口中的字符串是一个解
    #                 length = len(S[begin:i+1])
    #                 if length < minSize:  # 保留窗口长度更小的字符串
    #                     res = S[begin:i+1]
    #                 i = begin
    #                 temp = hashTable[:]  # 重新对temp分片赋值
    #         i += 1
    #     return res

    def minWindow(self, S, T):
        indices = {}
        for char in T:
            indices[char] = []    # 用字典存储T中每个字符在S中的序号
        llist = list(T)
        start = 0
        end = len(S)
        for i in xrange(len(S)):
            if S[i] in T:
                if S[i] not in llist and indices[S[i]] != []:  # T中的字符可能会重复，再次遇到T中的字符
                    indices[S[i]].pop(0)
                elif S[i] in llist:  # 每cover一个字符，列表中把该字符删除掉
                    llist.remove(S[i])
                indices[S[i]].append(i)  # 字典中存储该字符在S中的序号
                if len(llist) == 0:
                    maximum = max([x[-1] for x in indices.values()])  # 由于字符可能会重复，因此取最后遇到的字符的最大位置
                    minimum = min([x[0] for x in indices.values()])   # 取最开始遇到的字符的最小位置
                    if maximum - minimum + 1 < end - start + 1:
                        start = minimum
                        end = maximum
        if len(llist) > 0:
            return ''
        else:
            return S[start:end+1]



if __name__ == '__main__':
    s = Solution()
    print s.minWindow('aa', 'aa')
    print s.minWindow('bdab', 'ab')
    print s.minWindow('ADOBECODEBANC', 'ABC')

###################################################################################
# 一开始自己写的会超时。
# 用两个指针start和end记录cover所有T中字符的字符串起始位置和结束位置，用hashTable
# 记录T中每个字符在S中的位置，这里需要注意S和T中字符可能出现重复的情况，因此用列表
# 存储T中一个字符多次出现的位置。然后再用一个列表判断是否cover所有T中字符。
#