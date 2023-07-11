import pandas as pd
import numpy as np
import locale
locale.setlocale(locale.LC_ALL, '')# 转换数据类型
pf = 'qwq.txt'
d = pd.read_csv(pf)
fin = d.drop(d.index[[0,11,22,33,44,55,66,77,88,99,110]]) #去掉没有数据的行
f1 = fin['导演']
f2 = fin['票房']

list1 = [] #把导演名字做成列表
for x in f1:
    line = x
    list1.append(line)

list2 = [] #把票房做成列表
for y in f2:
    line = locale.atoi(y)
    list2.append(line)

list3 = list(set(list1)) #通过转换成集合再换回列表去掉重复出现的导演
#print(list3)
dict1 = {}
for i in list3:
    peo = np.array(list1)
    indexs = np.where(peo == i) #获取每个导演第一次出现时的list1列表索引值
    row_indices = indexs[0] #所有导演出现时的索引值
    #print(row_indices)
    l2_data = [list2[idx] for idx in row_indices] #获取对应行索引的list2数据
    l2_sum = sum(l2_data)  #对数据进行求和
    #print(peo[indexs[0][0]])  #打印每行的第一个元素
    #print(l2_sum) #打印对应导演的票房
    dict1[i] = {
        'name':peo[indexs[0][0]],
        'price':l2_sum
    }
dict2 = sorted(dict1.items(), key=lambda x: x[1]['price'],reverse=True)
for key, value in dict2:
    print(f"Name: {value['name']}")
    print(f"Price: {value['price']}")
    print()