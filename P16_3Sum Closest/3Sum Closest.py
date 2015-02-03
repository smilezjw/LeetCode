# coding=utf8

__author__ = 'smilezjw'


def threeSumClosest(num, target):
    num = sorted(num)
    distance = 2 ** 31 - 1
    if len(num) == 3:
        return num[0] + num[1] + num[2]
    else:
        for i in xrange(len(num)):
            p = i + 1
            q = len(num) - 1
            while p < q:
                temp = num[i] + num[p] + num[q]
                #distance.append(abs(target - temp))
                if abs(target - temp) < distance:
                    distance = abs(target - temp)
                    result = temp
                if temp == target:
                    result = temp
                    break
                elif temp > target:
                    q -= 1
                else:
                    p += 1
        return result


if __name__ == '__main__':
    print threeSumClosest([-1, 2, 1, -4], target=1)
    print threeSumClosest([0,2,1,-3], target=1)
    print threeSumClosest([1, 1, 1, 1], target=3)
    print threeSumClosest([-3,-2,-5,3,-4],target=-1)

###########################################################################################
# 这道题的思路和上一道题求三个数之和为0的思路是类似的。
# 首先将数组进行排序，然后有一个外层循环，里面从i+1和len(num)-1两头向中间遍历，
# 判断三个数之和与target的差是否最小。
# 这里如果用数组记录每一次三个数之后与target的差，则对于大数组会超时；
# 因此这里选择用变量distance判断三个数之后与target的差是否最小，赋予初值为正整数的最大值。