import ssl
ssl._create_default_https_context=ssl._create_unverified_context

from urllib import request
import requests
import re,random,time
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

## 搜索型产品
xiaomi="https://list.tmall.com/search_product.htm?q=%D0%A1%C3%D7%CA%D6%BB%FA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
hongmi="https://list.tmall.com/search_product.htm?q=%BA%EC%C3%D7%CA%D6%BB%FA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
vivo="https://list.tmall.com/search_product.htm?q=vivo%CA%D6%BB%FA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
oppo="https://list.tmall.com/search_product.htm?q=oppo%CA%D6%BB%FA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
iphone = 'https://list.tmall.com/search_product.htm?q=iphone&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'
anzhuo="https://list.tmall.com/search_product.htm?q=%B0%B2%D7%BF%CA%D6%BB%FA&type=p&spm=a220m.1000858.a2227oh.d100&xl=anzhuo%CA%D6%BB%FA_1&from=.list.pc_1_suggest"
huawei = 'https://list.tmall.com/search_product.htm?q=%BB%AA%CE%AA%CA%D6%BB%FA&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton'

## 体验型产品
lays="https://list.tmall.com/search_product.htm?q=%C0%D6%CA%C2%CE%DE%CF%DE%CA%ED%C6%AC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
szss="https://list.tmall.com/search_product.htm?q=%C8%FD%D6%BB%CB%C9%CA%F3&type=p&spm=a220m.1000858.a2227oh.d100&xl=sanzhi_1&from=.list.pc_1_suggest"
tsyl="https://list.tmall.com/search_product.htm?q=%CC%BC%CB%E1%D2%FB%C1%CF&type=p&spm=a220m.1000858.a2227oh.d100&xl=%CC%BC%CB%E1_1&from=.list.pc_1_suggest"
sp="https://list.tmall.com/search_product.htm?q=%CA%ED%C6%AC&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
xfs="https://list.tmall.com/search_product.htm?q=%CF%B4%B7%A2%CB%AE&type=p&spm=a220m.1000858.a2227oh.d100&xl=%CF%B4%B7%A2_1&from=.list.pc_1_suggest"
sg="https://list.tmall.com/search_product.htm?q=%CB%AE%B9%FB&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
cookie = 'cna=E897FHdj02MCAW64s0k7f4AI; _med=dw:1440&dh:900&pw:2880&ph:1800&ist:0; dnk=tb113149828; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&cookie14=Uoe1i6btcM1aVA%3D%3D&cookie21=VFC%2FuZ9ainBZ&pas=0&cookie15=VT5L2FSpMGV7TQ%3D%3D; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&nk2=F5REP7%2BSucQZoII%3D&id2=VyyVz5MMDi0wBg%3D%3D&vt3=F8dCuwlCjOZw%2Fsli2vA%3D; tracknick=tb113149828; lid=tb113149828; uc4=id4=0%40VXtaQW2ziVx2RBAHnoqo5bixKpPy&nk4=0%40FY4PbatQW9UBFWPYm1y9eUcRBFfRJQ%3D%3D; _l_g_=Ug%3D%3D; unb=4041432206; lgc=tb113149828; cookie1=UNdbC%2BPeiL7vstOw%2FJnT%2BTG6qNpQDfcV3by9Wo%2Bs%2F5Q%3D; login=true; cookie17=VyyVz5MMDi0wBg%3D%3D; cookie2=17fa2ef95985a5b9db80b246aba08cd9; _nk_=tb113149828; sgcookie=E1005QwqXEOlTCjLNGYySHwkqjc2oJj8ye1V6cemps%2BNKvfmA09ptvRczONPLDeQtdlo5oy96ZSGw6lhBQRDqR7HhQ%3D%3D; t=4121633cd59e3d8160d302d76f6ab8c7; sg=869; csg=fbdc36ba; enc=33FVoRAcft9zhUtcsw7OWVTHt3DDgIpjrbrWGwgLyQlzi0zv08gJ2iTusoCMfKbc0ouiQogPg90OjRq%2B5Yn5DQ%3D%3D; _tb_token_=f1eb36e8e9336; xlly_s=1; _m_h5_tk=7566afbe536c7bc1b238cb741a26e4fa_1619967860512; _m_h5_tk_enc=a01978a629f5b4787b233e57ca3e1c41; res=scroll%3A990*6541-client%3A135*806-offset%3A135*6541-screen%3A1440*900; pnm_cku822=098%23E1hvdQvUvbpvUpCkvvvvvjiWPLcy0jr2PFzhtjEUPmPptj1EnLSUtjYUP2Mh6j1WRd9Cvm9vvvvvphvvvvvvvhrvpvsZvvmmZhCv2CUvvUEpphvWh9vv9DCvpvQouvhvmvvv9b1rcax2kvhvC99vvOHtop9CvhQWa69vC0ErQjc6Di3%2Bju2W%2BW97%2B3%2Bda4oQD46OjomlKWVYRCBiBf7gQa7tnV3XQRLOlC%2B4axAQrfFCKdyIvWoy%2BbZcR2xVI42viC4AvvhvC9vhvvCvpvgCvvpvvvvvRvhvCvvvvvmevpvhvvmv99%3D%3D; tfstk=cCqPBQs0eDVjGgmCW0ieF4mndkhRZfZgvIkIrrzZuOMRMV3li0OKnYw-uVGOm4f..; l=eBjFh3wcjoKb8IksBOfwourza77OSIRAguPzaNbMiOCPOj1e5zWOW61EAz8wC3GVhsO6R3luRWdkBeYBcCDXrVmstBALurkmn; isg=BD4-QC9T0mdnSAZDgi-XRgX1j1KAfwL57jmdaehHqgF8i95lUA9SCWRhA1dHs_oR'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 wechatdevtools/0.7.0 MicroMessenger/6.3.9 Language/zh_CN webview/0'
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'cookie': cookie

}

def rate_spider(url,headers):
    '''
    :param url: 天猫搜索页
    :param headers: 爬虫请求头
    :return: 返回一个小数列表，列表的索引是排名，元素是评论数量
    '''
    req = requests.get(url=url, headers=headers)
    html = req.text
    reviews = re.findall(r'">(.+?)</a></span>',html)
    prices = re.findall(r';</b>(.+?)</em>',html)
    prices = [float(i) for i in prices]
    trades = re.findall(r'<em>(.+?)笔',html)

    rate = []
    for i in reviews:
        if i[-1]!='万':
            rate.append(float(i))
        else:
            rate.append(float(i[:-1])*10000)

    trade = []
    for i in trades:
        if i[-1]!='万':
            trade.append(float(i))
        else:
            trade.append(float(i[:-1])*10000)

    return rate,prices,trade

def rate_plot(rate,name):
    plt.style.use('ggplot')
    x = np.arange(len(rate))
    x += 1
    x_ticks = list(range(0,len(rate)+1,5))
    x_ticks[0] = 1
    plt.plot(x,rate)
    plt.title(name+" Sales Rank and Number of Reviews")
    plt.xlabel("Sales rank")
    plt.ylabel("Number of Reviews")
    plt.xticks(x_ticks)
    plt.savefig(f'./res/{name}.png')
    plt.show()

def calc_corr(a, b):
    a_avg = sum(a) / len(a)
    b_avg = sum(b) / len(b)
    # 计算分子，协方差————按照协方差公式，本来要除以n的，由于在相关系数中上下同时约去了n，于是可以不除以n
    cov_ab = sum([(x - a_avg) * (y - b_avg) for x, y in zip(a, b)])
    # 计算分母，方差乘积————方差本来也要除以n，在相关系数中上下同时约去了n，于是可以不除以n
    sq = math.sqrt(sum([(x - a_avg) ** 2 for x in a]) * sum([(x - b_avg) ** 2 for x in b]))
    corr_factor = cov_ab / sq
    return corr_factor

def regression_analysis(X,y):
    x_in=np.array(X).reshape(-1,1)
    y_in=np.array(y).reshape(-1,1)
    lrg1 = LinearRegression()
    lrg1.fit(x_in, y_in)
    return get_lr_stats(x_in, y_in, lrg1)
    # plt.scatter(x_in, y_in)
    # plt.show()


#### 统计量参数

def get_lr_stats(x, y, model):
    message0 = f'一元线性回归方程为: \ty={model.intercept_[0]:.3f} + {model.coef_[0][0]:.3f}*x'
    from scipy import stats
    n     = len(x)
    y_prd = model.predict(x)
    Regression = sum((y_prd - np.mean(y))**2) # 回归
    Residual   = sum((y - y_prd)**2)          # 残差
    R_square   = Regression / (Regression + Residual) # 相关性系数R^2
    F          = (Regression / 1) / (Residual / ( n - 2 ))  # F 分布
    pf         = stats.f.sf(F, 1, n-2)
    message1 = (f'相关系数(R^2)： {R_square[0]:.3f}；\n' +
                f'回归分析(SSR)： {Regression[0]:.3f}；\t残差(SSE)：{Residual[0]:.3f}；\n' +
                f'           F ： {F[0]:.3f}；\tpf ： {pf[0]}')
    ## T
    L_xx  =  n * np.var(x)
    sigma =  np.sqrt(Residual / (n-2))
    t     =  model.coef_ * np.sqrt(L_xx) / sigma
    pt    =  stats.t.sf(t, n-2)
    message2 = f'           t ： {t[0][0]:.3f}；\tpt ： {pt[0][0]}'
    return R_square[0]




def rerank(trade,review,price):
    c = sorted(zip(trade, review, price), key=lambda x: x[0],reverse=True)
    new_trade=[]
    new_review=[]
    new_price=[]
    for i,j,k in c:
        new_trade.append(i)
        new_review.append(j)
        new_price.append(k)
    return new_trade,new_review,new_price

def liucheng(urla,name):
    review,price,trade=rate_spider(urla,headers=headers)
    new_trade, new_review, new_price = rerank(trade, review, price)
    pearson=calc_corr(new_trade,new_review)
    R2=regression_analysis(new_trade, new_review)
    rate_plot(new_review, name)
    return pearson,R2

if __name__=="__main__":
    names1=['iPhone','Android','xiaomi','hongmi','vivo','oppo','huawei']
    search_p=[iphone,anzhuo,xiaomi,hongmi,vivo,oppo,huawei]
    names2=['drinks','crisps','shampoo','Lays','Three squirrels', 'fruit']
    experi_p = [tsyl, sp, xfs, lays, szss, sg]
    dict1={}
    dict2={}
    for i in range(len(names1)):
        result1=[]
        p,r=liucheng(search_p[i],names1[i])
        result1.append(p)
        result1.append(r)
        dict1[names1[i]]=result1
    for i in range(len(names2)):
        result1=[]
        p,r=liucheng(experi_p[i],names2[i])
        result1.append(p)
        result1.append(r)
        dict2[names2[i]]=result1
    print(dict1)
    print(dict2)
    # print(new_trade)
    # print(new_review)
    # rate_plot(android_rate,"Android Phones")
    # iphone_rate, iphone_price, iphone_trade = rate_spider(url_2,headers=headers)
    # del_index = [7,8,10,21,23,43,54]
    # iphone_price = [i for num, i in enumerate(iphone_price) if num not in del_index]
    # print(iphone_trade)
    # rate_plot(iphone_rate,"Iphones")



