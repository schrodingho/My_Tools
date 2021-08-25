import numpy as np
def recall_at_k(predict,test,k):
    return None

def ndcg_at_k(predict,test,k):
    ndcg_array = np.zeros((np.shape(test)[0],))
    for j in range(np.shape(predict_matrix)[0]):
        idx = np.argsort(-predict_matrix[j, :])[:k]
        ground_truth = test[j, idx]
        ndcg_gt = np.ones((len(ground_truth),))
        iter_ndcg = np.sum((2 ** ground_truth - 1) / np.log2(np.arange(2, k + 2))) / np.sum(
            (2 ** ndcg_gt - 1) / np.log2(np.arange(2, k + 2)))
        ndcg_array[j] = iter_ndcg


def map_at_k(predict,test,k):
    return None

def NDCG_binary_at_k_batch(train_data, heldout_data, Et, Eb, user_idx,
                           mu=None, k=100, vad_data=None):
    batch_users = user_idx.stop - user_idx.start
    X_pred = _make_prediction(train_data, Et, Eb, user_idx,
                              batch_users, mu=mu, vad_data=vad_data)
    return_array=np.zeros((1001,))
    for i in range(len(X_pred)):
        idx10=np.argsort(-X_pred[i,:])[:k]
        test_real10=heldout_data.A[i,idx10]
        ndcg10_gt=np.ones((k,))
        iter_ndcg10=np.sum((2**test_real10-1)/np.log2(np.arange(2, k+2)))/np.sum((2**ndcg10_gt-1)/np.log2(np.arange(2,k+2)))
        return_array[i]=iter_ndcg10
    return return_array