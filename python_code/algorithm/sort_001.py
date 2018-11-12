
li = [77, 92, 67, 8, 6, 84, 55, 95, 43, 67]

for x in range(len(li)):
    print('x: ',x)
    for y in range(x+1,len(li)):
        print('y: ',y)
        maxItem = li[x]
        if li[y] > li[x]:
            print(li[x], li[y])
            li[x] = li[y]
            li[y] = maxItem
            print(li[x], li[y])
            print(li[:])
