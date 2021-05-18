# this file is for calculating the pearson coefficient by two vectors
# this file is also for calculating jaccard coefficient
import pandas as pd
import math
import numpy as np


# 函数：计算相关系数
def calc_corr(a, b):
    a_avg = sum(a) / len(a)
    b_avg = sum(b) / len(b)
    # 计算分子，协方差————按照协方差公式，本来要除以n的，由于在相关系数中上下同时约去了n，于是可以不除以n
    cov_ab = sum([(x - a_avg) * (y - b_avg) for x, y in zip(a, b)])
    # 计算分母，方差乘积————方差本来也要除以n，在相关系数中上下同时约去了n，于是可以不除以n
    sq = math.sqrt(sum([(x - a_avg) ** 2 for x in a]) * sum([(x - b_avg) ** 2 for x in b]))
    corr_factor = cov_ab / sq
    return corr_factor


def jaccard(v1, v2):
    import scipy.spatial.distance as dist
    matv = np.array([v1, v2])
    ds = dist.pdist(matv, 'jaccard')[0]
    return 1 - ds


if __name__ == '__main__':
    # first step: ensure the drugs that should be accounted
    # missing = 0; not_missing = 1
    # no = 0; yes = 1
    # a = [0,1,0,1,1,1]
    # b = [0,0,1,1,0,0]
    # b_s = pd.Series(b)
    # a_s = pd.Series(a)
    # cor1 = a_s.corr(b_s)
    #
    # # 自编函数计算两个列表的相关系数
    # cor2 = calc_corr(a, b)
    # # 可以发现两者结果是一样的
    # print(cor1, cor2)

    x = [0, 0, 0]
    y = [0, 0, 0]
    print(jaccard(x, y))