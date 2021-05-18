def AP(ranked_list, ground_truth):
    """Compute the average precision (AP) of a list of ranked items
    ground_truth 表示是否正确的标识
    hits 表示 score （预测结果分值）倒排，从第0个到当前个的累计预测正确样本数
    sum_precs 表示每个 ground_truth = 1 的位置的 precision 的累加
    """
    hits = 0
    sum_precs = 0
    for n in range(len(ranked_list)):
        if ranked_list[n] in ground_truth:
            hits += 1
            sum_precs += hits / (n + 1.0)
    if hits > 0:
        return sum_precs / len(ground_truth)
    else:
        return 0
l1 = [1,1,1,0,0]
l2 = [1,1,1,1,1]
print(AP(l1,l2))
