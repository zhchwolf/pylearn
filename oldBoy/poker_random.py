import random
getlist=[]
zero_num = 0
for i in range(5):
    getlist.append(random.randint(0,13))

print('complete list:', getlist[:])
while 0 in getlist :
    getlist.remove(0)
    zero_num += 1

print(getlist[:])
print(min(getlist[:]))
print(max(getlist[:]))





