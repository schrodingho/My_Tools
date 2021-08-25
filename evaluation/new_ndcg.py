import numpy as np
import pandas as pd

def ndcg_at_k(predict, test, k):
    ndcg_array = np.zeros((np.shape(test)[0],))
    for j in range(np.shape(test)[0]):
        if np.sum(test[j, :]) != 0:
            if np.sum(test[j, :]) >=k:
                hit=k
            else:
                hit=np.sum(test[j, :])
            idx = np.argsort(-predict[j, :])[:hit]
            ground_truth = test[j, idx]
            ndcg_gt = np.ones((hit,))
            iter_ndcg = np.sum((2 ** ground_truth - 1) / np.log2(np.arange(2, hit + 2))) / np.sum(
                (2 ** ndcg_gt - 1) / np.log2(np.arange(2, hit + 2)))
            ndcg_array[j] = iter_ndcg
        else:
            ndcg_array[j] = np.nan
    return np.nanmean(ndcg_array)

ground_truth = np.array([1,1,1,0,0])
ndcg_gt = np.array([1,1,1,1,1])
print(np.sum((2 ** ground_truth - 1) / np.log2(np.arange(2, 5 + 2))) / np.sum(
                (2 ** ndcg_gt - 1) / np.log2(np.arange(2, 5 + 2))))

