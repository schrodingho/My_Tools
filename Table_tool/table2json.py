import xlrd
from collections import OrderedDict
import json
# import pandas as pd
#
# df=pd.read_excel('summer_camp.xlsx')
# print(df['ddl'])

wb = xlrd.open_workbook('summer_camp.xlsx')

convert_list = []
sh = wb.sheet_by_index(0)
title = sh.row_values(0)
for rownum in range(1, sh.nrows):
    rowvalue = sh.row_values(rownum)
    single = {}
    for colnum in range(0, len(rowvalue)):
        print(title[colnum], rowvalue[colnum])
        single[title[colnum]] = rowvalue[colnum]
    convert_list.append(single)

print(convert_list)
# j = json.dumps(convert_list)
#
# with codecs.open('file.json', "w", "utf-8") as f:
#     f.write(j)
{'name': '复旦大学', 'faculty': '经济学院', 'id': '2021年复旦大学经济学院第三届全国优秀本科生直接攻博夏令营活动报名通知', 'level': '985', 'ddl': '2021.5.20', 'url': 'https://econ.fudan.edu.cn/info/1307/18625.htm'}, {'name': '复旦大学', 'faculty': '经济学院', 'id': '2021年复旦大学经济学院第十届金融专硕全国优秀大学生夏令营活动报名通知（专业学位）', 'level': '985', 'ddl': '2021.5.20', 'url': 'https://econ.fudan.edu.cn/info/1519/18624.htm'}, {'name': '上海交通大学', 'faculty': '上海高级金融学院', 'id': '上海高级金融学院金融硕士2022级推免招生公告', 'level': '985', 'ddl': '分批次', 'url': 'http://mf.saif.sjtu.edu.cn/show-145-723.html'}, {'name': '清华大学', 'faculty': '经济管理学院', 'id': '清华-哥大商务分析硕士', 'level': '985', 'ddl': '分批次', 'url': 'https://masters.sem.tsinghua.edu.cn/geda/gyshenq.html'}, {'name': '吉林大学', 'faculty': '行政学院', 'id': '吉林大学行政学院2021年北辰夏令营', 'level': '985', 'ddl': '2021.4.21', 'url': 'http://adm.jlu.edu.cn./info/1109/21974.htm'}, {'name': '清华大学', 'faculty': '自动化系', 'id': '清华大学自动化系智能与网络化系统研究中心2021年招生夏令营', 'level': '985', 'ddl': '2021.4.15', 'url': 'https://mp.weixin.qq.com/s/xyoqcOVdxctfmCUKGiPGwg'}, {'name': '南方科技大学', 'faculty': '化学系', 'id': '南方科技大学化学系2021年全国优秀大学生夏令营', 'level': '双非', 'ddl': '未定', 'url': 'http://chem.sustc.edu.cn/#/zh/news/details/250'}, {'name': '北京大学', 'faculty': '数学科学学院', 'id': '2022年北大数学学科直博生摸底考试', 'level': '985', 'ddl': '2021.4.4', 'url': 'https://www.math.pku.edu.cn/zygg/126019.htm'}]


