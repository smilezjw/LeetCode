# _*_ coding:utf8 _*_

__author__ = 'smilezjw'

def twoSum(num, target):
    #首先是我自己的写法。。弱爆了
    # for n1 in num:
    #     for n2 in num:
    #         if n1 + n2 == target:
    #             index1 = num.index(n1)
    #             index2 = num.index(n2)
    #             found = True
    # if found is True:
    #     return (min(index1,index2), max(index1, index2))
    # else:
    #     return 'Not found!'

    #一遍扫描num，看Hash表中的数有没有target - x，如果有则直接返回index，否则将x放入hash表中
    dict = {}     #构建Hash表
    for i, n in enumerate(num):
        if dict.get(target - n,None) != None:
            return (dict[target - n] + 1, i + 1)
        dict[n] = i

if __name__ == '__main__':
    print twoSum(num=[0, 4, 3, 0], target=0)
    print twoSum(num=[2, 7, 11, 15], target=9)

    ###############################################
    # 1. Brute force ---- O(n^2) runtime, O(1) space
    # Loop through each element x and find if there is another value that equals to target-x.
    # As finding another value requires looping through the rest of value, its runtime complexity is O(n^2)
    #
    # 2. Hash table ---- O(n) runtime, O(n) space
    # We could reduce the runtime complexity of looking aup a value to O(1) using a hash map that
    # maps a value to its index.