# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def isMatch(self, s, p):
        sLen = len(s)
        pLen = len(p)
        # sPointer记录遍历s字符串的指针
        # pPointer记录遍历p字符串的指针
        # ss记录遇到*时sPointer的位置
        pPointer = sPointer = ss = 0
        star = -1
        while sPointer < sLen:
            # 如果pPointer指向？或者p[pPointer] == s[sPointer]，说明匹配，两个指针分别指向下一个字符
            if pPointer < pLen and (p[pPointer] == '?' or p[pPointer] == s[sPointer]):
                sPointer += 1
                pPointer += 1
            # 如果pPointer指向* 则star记录pPointer当前位置，ss记录sPointer当前位置
            # 这里pPointer加1但是sPointer不加1，是因为*可以匹配空字符串
            elif pPointer < pLen and p[pPointer] == '*':
                star = pPointer
                pPointer += 1
                ss = sPointer
            # 如果当前两个指针指向的字符不匹配，则pPointer被拉回到*的下一个位置，
            # sPointer指向ss的下一个位置，ss在这里也需要加1，因为ss表示*能够匹配到的位置
            elif star != -1:
                pPointer = star + 1
                ss += 1
                sPointer = ss
            # 如果没有*，则直接返回False
            else:
                return False
        # s字符串走完p中还可能剩下*，如果p中除了*还有其他字符，则返回False
        while pPointer < pLen and p[pPointer] == '*':
            pPointer += 1
        return pPointer == pLen


if __name__ == '__main__':
    s = Solution()
    print s.isMatch('aa', 'a')
    print s.isMatch('aa', 'aa')
    print s.isMatch('aaa', 'aa')
    print s.isMatch('aa', '*')
    print s.isMatch('aa', 'a*')
    print s.isMatch('ab', '?*')
    print s.isMatch('aab', 'c*a*b')