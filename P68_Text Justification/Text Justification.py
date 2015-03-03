# coding=utf8

__author__ = 'smilezjw'


class Solution:
    # def fullJustify(self, words, L):
    #     if words == ['']:
    #         return [' '*L]
    #     res = []
    #     curr = ''
    #     w = 0
    #     while w < len(words):
    #         if len(curr) + len(words[w]) <= L:
    #             curr += words[w] + ' '
    #             w += 1
    #         elif len(curr.split()) == 1:
    #             curr = curr[:-1]
    #             spacesNum = L - len(curr)
    #             curr += ' ' * spacesNum
    #             res.append(curr)
    #             curr = ''
    #         elif len(curr.split()) > 1:
    #             curr = curr.split()
    #             spacesNum = L - len(''.join(curr))
    #             evenSpace = spacesNum / (len(curr) - 1)
    #             space = spacesNum % (len(curr) - 1)
    #             temp = ''
    #             if space > 0:
    #                 for i in xrange(len(curr)-2):
    #                     temp += curr[i] + ' ' * (evenSpace + space)
    #                 temp += curr[-2] + ' ' * evenSpace + curr[-1]
    #             else:
    #                 for i in xrange(len(curr)-1):
    #                     temp += curr[i] + ' ' * evenSpace
    #                 temp += curr[-1]
    #             res.append(temp)
    #             curr = ''
    #         elif w == len(words) - 1:
    #             curr = curr[:-1]
    #             spacesNum = L - len(curr)
    #             curr += ' ' * spacesNum
    #             res.append(curr)
    #             curr = ''
    #     if curr != '':
    #         curr = curr[:-1]
    #         spacesNum = L - len(curr)
    #         curr += ' ' * spacesNum
    #         res.append(curr)
    #     return res

    def fullJustify(self, words, L):
        res = []
        i = 0
        while i < len(words):
            size = 0
            begin = i
            while i < len(words):
                if size == 0:
                    newsize = len(words[i]) + size
                else:
                    newsize = len(words[i]) + size + 1  # 加1是因为加上一个空格的长度
                if newsize <= L:
                    size = newsize
                else:
                    break
                i += 1
            spaceCount = L - size  # 计算extra space的数量
            if i - begin - 1 > 0 and i < len(words):  # 不只有一个单词并且不是最后一行
                everyCount = spaceCount / (i - begin - 1)  # 计算平均每两个单词之间extra space的数量
                spaceCount %= i - begin - 1  # 计算依然多余不平均的extra space数量
            else:
                everyCount = 0  # 如果是只有一个单词或者是最后一行，那么单词之间的空格为0
            j = begin
            while j < i:
                if j == begin:
                    s = words[j]
                else:
                    # 原来每两个单词之间有一个空格，然后加上平均extra space； 如果是最后一行的话，每两个单词之间只有一个空格
                    s += ' ' * (everyCount+1)
                    if spaceCount > 0 and i < len(words):
                        s += ' '  # 还有不均匀分布的extra space
                        spaceCount -= 1
                    s += words[j]
                j += 1
            s += ' '*spaceCount  # 如果只有一个单词或者是最后一行，那么extra space都加在右边
            res.append(s)
        return res

if __name__ == '__main__':
    s = Solution()
    print s.fullJustify([''], 0)
    print s.fullJustify([''], 2)
    print s.fullJustify(["a","b","c","d","e"], 1)
    print s.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], L=16)
    print s.fullJustify(["Here","is","an","example","of","text","justification."], 15)
    print s.fullJustify(["My","momma","always","said,","'Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."], 20)

############################################################################################
# 这道题是细节题，很不容易完整写出来。主要需要注意两点：1.如果该行只有一个单词时，空格全部在
# 右边；2.最后一行单词之间只有一个空格，其余空格全部再右边。然后贪心选择，每一行中尽量多放单
# 词。在计算每两个单词之间的空格时，需要考虑3部分：原来每两个单词之间就有一个空格，然后extra
# space均匀分布在各个单词之间的数量，还有就是依然还剩余下来不能均匀分布的空格数量，这一部分在
# 每两个单词之间加1直至加完。
#