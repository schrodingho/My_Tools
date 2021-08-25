import random
import pandas as pd
import numpy as np


def k_fold_split(train, k):
    k_fold = []
    index = set(range(train.shape[0]))
    for i in range(k):
        # 防止所有数据不能整除k，最后将剩余的都放到最后一折
        if i == k - 1:
            k_fold.append(list(index))
        else:
            tmp = random.sample(list(index), int(1.0 / k * train.shape[0]))
            k_fold.append(tmp)
            index -= set(tmp)
    # 将原始训练集划分为k个包含训练集和验证集的训练集，同时每个训练集中，训练集：验证集=k-1:1
    for i in range(k):
        print("第{}折........".format(i + 1))
        tra = []
        dev = k_fold[i]
        for j in range(k):
            if i != j:
                tra += k_fold[j]
        train.iloc[tra].to_csv("data/train_{}".format(i), sep=" ", index=False, header=False)
        train.iloc[dev].to_csv("data/val_{}".format(i), sep=" ", index=False, header=False)
    print("done!")
