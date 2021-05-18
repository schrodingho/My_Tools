import numpy as np


def getDCG(scores):
    return np.sum(np.divide(np.power(2, scores) - 1, np.log2(np.arange(scores.shape[0], dtype=np.float32) + 2)),
        dtype=np.float32)

def getNDCG2(rank_list,pos_items):
    relevance=np.ones_like(pos_items)
    rank_scores=np.asarray(rank_list, dtype=np.float32)
    idcg = getDCG(relevance)
    dcg = getDCG(rank_scores)
    if dcg == 0.0:
        return 0.0
    ndcg = dcg / idcg
    return ndcg

def getNDCG(rank_list, pos_items):
    relevance = np.ones_like(pos_items)
    it2rel = {it: r for it, r in zip(pos_items, relevance)}
    rank_scores = np.asarray([it2rel.get(it, 0.0) for it in rank_list], dtype=np.float32)

    idcg = getDCG(relevance)

    dcg = getDCG(rank_scores)

    if dcg == 0.0:
        return 0.0

    ndcg = dcg / idcg
    return ndcg
l1 = [1,1,1,0,0]
l2 = [1,1,1,1,1]

print(getNDCG(l1, l2))
print(getNDCG2(l1, l2))




# 0.4692787