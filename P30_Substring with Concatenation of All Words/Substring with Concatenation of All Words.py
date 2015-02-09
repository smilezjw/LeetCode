# coding=utf8

__author__ = 'smilezjw'


# def findSubstring(S, L):  # 这种做法使得S='aaa',L=['a','b']返回[0,1]，因为没有考虑S中连续重复字符串
#     temp = []
#     res = []
#     len_L = len(L[0])
#     len_S = len(S)
#     counts = len(L)
#     for i in xrange(len_S - len_L * counts + 1):
#         temp = []
#         for j in xrange(i, (i + len_L * counts), len_L):
#             if S[j: j+len_L] in L:
#                 temp.append(j)
#             else:
#                 break
#         if len(temp) == counts:
#             res.append(temp[0])
#     return res

def findSubstring(S, L):
    res = []
    lenL = len(L[0])
    lenS = len(S)
    counts = len(L)
    for i in xrange(lenS-lenL*counts+1):
        # 同样构造长度为counts的列表，其中每个字符串长度为lenL
        seg = [S[j: j+lenL] for j in xrange(i, (i + lenL * counts), lenL)]
        for p in L:
            if p in seg:
                # remove一次只删除一个元素（即使存在重复元素的情况）这样避免了出现重复连续字符串的情况
                seg.remove(p)
            else:
                break
        if seg == []: # 表示全部匹配，则最前面的下标i添加到结果列表中
            res.append(i)
    return res

if __name__ == '__main__':
    print findSubstring('barfoothefoobarman',['foo','bar'])
    print findSubstring('aaa', ['a', 'b'])

################################################################################################
# 这道题一开始的思路大致是对的，但是没有考虑连续重复出现字符的情况，因此选用第二种算法用remove
# 则可以避免这种情况。总体感觉字符串的题目比较好理解好下手。
