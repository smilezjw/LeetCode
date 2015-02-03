# coding=utf8

__author__ = 'smilezjw'


def threeSum(num):
    num = sorted(num)       # 先对数组进行排序，这样正数和负数就可以分开来了
    result = []
    if len(num) <= 2:
        return result
    else:
        for i in xrange(len(num)):
            if num[i] > 0:  # 如果已经是正数了，那三个数相加肯定不为0
                break
            p = i + 1       # 从两头往中间遍历
            q = len(num) - 1
            while p < q:
                if num[i] + num[p] + num[q] == 0:
                    solution = sorted([num[i], num[p], num[q]])
                    if solution not in result:
                        result.append(solution)
                    p += 1
                    q -= 1
                # 如果三个数相加小于0，由于q已经是最大了，只能使p变大
                elif num[i] + num[p] + num[q] < 0:
                    p += 1
                # 如果三个数相加大于0，由于p已经是最小了，只能使q变小
                else:
                    q -= 1
        return result

if __name__ == '__main__':
    print threeSum([-1, 0, 1, 2, -1, -4])
    print threeSum([1,-1])


#####################################################################################################
# 时间复杂度为O(n^2),首先需要对数组进行排序，这样正数和负数就分开来了。
# 有一个外层循环遍历数组，另外两个数从两头往中间遍历，从i+1和len(num)-1往中间遍历；
# 如果三个数相加大于0，由于p已经最小了，因此只能移动q使得num[q]减小；
# 如果三个数相加小于0，由于q已经最大了，因此只能移动p使得num[p]增大。
# 如果外层循环的数已经大于0了，那么三个数相加肯定大于0，则直接跳出外层循环。