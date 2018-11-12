#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# 爱奇艺累计有2000万会员，为了提高会员权益以及减少运营成本，我们需要对用户分等级差异化运营，为此我们制定了用户成长体系，按成长值（最小为0）划分为不同等级。成长值计算公式为：
# 会员成长值＝每天成长值＋任务成长值
# 现在我们输入一组数据，表示用户的成长值计算规则，比如某个用户的每天成长值规则1 1 5 10，第一列1表示每日成长值规则，第二列1表示该条规则的生效开始时间，第三列5表示该条规则的生效截至时间，第四列10表示该条规则的每天成长值，则用户初始值为0，第1天到第5天，每天成长值10点，则第5天成长值为50；
# 另外任务成长值规则，比如2 3 4，第一列2表示该规则为任务成长值，第二列3表示第三天做任务，第三列4表示该天做任务得到成长值4。现在输入一组数据，每行一条成长规则，每日成长规则生效时间重合时以成长数值最大的为准，每日成长值是每天0点更新，任务成长值是0点以后，要求计算成长值规则对应最后一天成长值。
# 输入
# 输入数据有多行，第一列为1时，该行会有4个数值，第一列为2时，该列会有3个数值
# 输出
# 对于每个测试实例，初始成长值都为0，计算成长值规则最后一天的用户成长值。
#
# 样例输入
# 1 1 5 10
# 2 3 4
# 1 4 6 －5
# 样例输出
# 49
from  functools import partial
inputNew = partial(input, 'input growth value end by "endl":')
sentinel = 'endl'
lines = []
valist = []
dvalue = 0

for line in iter(inputNew,sentinel):
    lines.append(line)

def getGrowthValue(rd):
    if rd[0] == 1:
        dvalue = (rd[2] - rd[1] + 1) * rd[3]
        print(dvalue)
    if rd[0] == 2:
        tvalue = (rd[2] - rd[1]) * rd[3]
        print(tvalue)
        return tvalue

for values in lines:
    valist = values.split()
    print(valist)
    print(len(valist), ' ', valist[0])
    if len(valist) == 4:
        print(valist[3])
        #and valist[0] == 1
        #dvalue = dvalue + getGrowthValue(valist)
        #print(dvalue)
    elif valist[0] == 1 and len(valist) != 4:
        print(valist, ' is illegal.')
        print('2')
    elif  valist[0] == 2 and len(valist) == 3:
        print(valist[3])
        for i in lines:
            ilist = i.split()
            if ilist[0] == 1 and len(ilist) == 4:
                if valist[1] > ilist[1] and valist[1] < ilist[2] and valist[2] > ilist[3]:
                    dvalue += getGrowthValue(valist)
#print(dvalue)
def sumGrowthValue():
    str4 = '1 1 20 10'
    str3 = '2 3 4'
    str5 = '1 4 6 －5'
    growthvalue1 = getGrowthValue(str4)
    growthvalue1 += getGrowthValue(str4)
    growthvalue1 += getGrowthValue(str4)
    print()

