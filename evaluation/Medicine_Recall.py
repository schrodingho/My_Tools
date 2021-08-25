import numpy as np
import pandas as pd



def med_re(predict,all,num):
    for i in range(np.shape(all)[0]):
        if i in num:
            length_i = np.sum(all[i,:])
            print(f"num_p: {i}, med_cnt: {length_i}")
            idx = np.argsort(-predict[i, :])[:length_i]
            real=all[i,idx]
            print(np.where(all[i,:] != 0))
            print(idx)
            print(idx*real)







if __name__=='__main__':
    med_re()