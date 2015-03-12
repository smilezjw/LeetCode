# coding=utf8

__author__ = 'smilezjw'


class Solution:
    def restoreIpAddresses(self, s):
        Solution.res = []
        self.dfs(s, 0, 0, [])
        return Solution.res

    def dfs(self, s, start, length, ip):
        if len(ip) == 4:  # ip地址为4段
            if length == len(s):  # length记录当前使用过s中的数字个数，如果全部用完了，则为一个解
                Solution.res.append('.'.join(ip))
            return
        for i in xrange(1, 4):  # ip地址每一段都是1到3个数字
            if (start+i) < len(s)+1:
                # ip地址每一段都在0~255范围内，但是排除00,000,001这样的情况
                if i == 1 or (0 < int(s[start:start+i]) <= 255 and s[start] != '0'):
                    # 参数传进去时修改，返回的时候还是原来的值
                    self.dfs(s, start+i, length+i, ip + [s[start:start+i]])
        return

if __name__ == '__main__':
    s = Solution()
    print s.restoreIpAddresses('0000')
    print s.restoreIpAddresses('010010')
    print s.restoreIpAddresses('25525511135')

#####################################################################################
# 深度优先搜索，第一次自己能够完整地写出来递归的题目，好棒！
# 主要还是在传递参数的时候要注意，一开始length += i，然后再在调用self.dfs()时传递参数
# length，那这样返回的时候length其实已经改变了，需要length-=i。
# 另外就是还需要注意00,01,000等这种数字的情况，这在ip地址中是不存在的。
#