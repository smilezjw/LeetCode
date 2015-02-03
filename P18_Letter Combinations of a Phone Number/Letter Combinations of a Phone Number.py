# coding=utf8

__author__ = 'smilezjw'


def letterCombinations(digits):
    d = {'0': '',
         '1': '',
         '2': ['a','b','c'],
         '3': ['d','e','f'],
         '4': ['g','h','i'],
         '5': ['j','k','l'],
         '6': ['m','n','o'],
         '7': ['p','q','r','s'],
         '8': ['t','u','v'],
         '9': ['w','x','y','z']}
    if len(digits) == 0:
        return ['']
    if len(digits) == 1:
        return d[digits[0]]
    else:
        result = []
        for i in d[digits[0]]:
            result.append(i)
        temp = result[:]
        for n in xrange(1, len(digits)):
            count = 0
            for s in temp:
                for i in d[digits[n]]:
                    result.append(s+i)
                    count += 1
            result[:len(result) - count] = ''
            temp[:] = result[:]
    return result

if __name__ == '__main__':
    print letterCombinations('23')
    print letterCombinations('2')

###############################################################################################
# 这道题刚拿到手想要用两个指针循环发现不能实现目的，后来就想一个数字一个数字对应的累加上去。
# 首先初始化列表为第一个数字对应的字母，然后逐个和后面的数字用循环进行笛卡尔积，
# 需要注意的是要更新列表，否则会出现死循环。
# 在实现过程中，遇到了一个错误，temp = result，这里的temp和result指向同一个对象，如果需要将
# 一个列表复制两份，则需要分片赋值： temp = result[:]，这样才能避免两者指向同一个对象。
#