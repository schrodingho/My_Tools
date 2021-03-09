#多级表格存为字典
import pandas as pd
import numpy as np
new=pd.read_excel('major.xlsx')
s1=np.array(new['门类'])
s2=list(np.array(new['专业类']))
s3=list(np.array(new['专业名称']))

def balabala(s2):
    dict_cnt2 = {}
    for item in s2:
        if item in dict_cnt2:
            dict_cnt2[item] += 1
        else:
            dict_cnt2[item] = 1
    return dict_cnt2

dict_cnt = balabala(s1)
sum=0
sum1 = 0
new2_dict={}
for i,j in dict_cnt.items():
    temp1=s2[sum:j+sum]
    sum=j+sum
    new1=balabala(temp1)
    new2={}
    for k,l in new1.items():
        temp2=s3[sum1:l+sum1]
        sum1=sum1+l
        new2[k]=temp2
    new2_dict[i]=[new2]
print(new2_dict)




