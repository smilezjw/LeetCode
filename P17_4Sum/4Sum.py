# coding=utf8

__author__ = 'smilezjw'


def fourSum(num, target):
    # num = sorted(num)
    # result = []
    # i = 0
    # j = len(num) - 1
    # while i < j:
    #     length = j - i
    #     p = i + 1
    #     q = j - 1
    #     while p < q:
    #         temp = num[i] + num[j] + num[p] + num[q]
    #         quadruplet = sorted([num[i], num[p], num[q], num[j]])
    #         if temp == target:
    #             if quadruplet not in result:
    #                 result.append(quadruplet)
    #             p += 1
    #             q -= 1
    #         elif temp > target:
    #             q -= 1
    #         elif temp < target:
    #             p += 1
    #     if num[i] + num[j] == target:
    #         j -= 1
    #         i += 1
    #     elif num[i] + num[j] > target:
    #         j -= 1
    #     else:
    #         i += 1
    # return result

    length = len(num)
    d = {}
    result = set()  #无序无重复元素集 unordered collections of unique elements
    if length < 4:
        return []
    num = sorted(num)
    for i in xrange(length):
        for j in xrange(i+1, length):
            sum1 = num[i] + num[j]
            if sum1 not in d:
                d[sum1] = [(i, j)]      # 字典的key为数组中每两个元素的和
            else:
                d[sum1].append((i, j))  # 字典的value为两个元素的下标组成的元祖
    for p in xrange(len(num)):
        for q in xrange(p+1, len(num)-2):
            x = target - num[p] - num[q]
            if x in d:                  # 检查target - 两个元素的和是否在字典的key中
                for (i, j) in d[x]:
                    if i > q:           # p < q < i < j  =>  num[p] < num[q] < num[i] < num[j]
                        result.add((num[p], num[q], num[i], num[j]))
    return [list(i) for i in result]   # 将set()类型转换成list类型输出


if __name__ == '__main__':
    print fourSum([1, 0, -1, 0, -2, 2], target=0)
    print fourSum([-3, -1, 0, 2, 4, 5], target=0)
    print fourSum([-3, -1, 0, 2, 4, 5], target=2)
    print fourSum([-3,-2,-1,0,0,1,2,3], target=0)

##########################################################################################
# 用哈希表增加空间复杂度来降低时间复杂度。
# 首先建立字典，字典的key为数组中每两个元素的和，对应的value为两个元素的下标组成的元组。
# 检查target - 两个元素的和 是否在字典的key中，如果存在并且下标符合顺序要求，则为一组解。
# 由于需要去重， 使用set()无序无重复元素集，最后将set()转换成list类型。