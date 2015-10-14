# coding=utf8

__author__ = 'smilezjw'


class Solution(object):
    def canWinGame(self, n):
        return n % 4 > 0


########################################################################################
# 当 n 属于[1, 3]， 先手必胜；
# 当 n == 4，无论先手如何选取，下一轮都会转化为 n 属于[1, 3]，先手必输；
# 当 n 属于[5, 7]，先手分别取走1， 2， 3颗石头，即可将状态转化为n == 4的情况，后手必输，先手必胜；
# 当 n == 8，无论先手如何选取，下一轮都会转化为 n 属于[5， 7]， 此时先手必输；
# 以此类推。。。
#