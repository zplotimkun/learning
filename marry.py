mencount = int(input('請輸入男性人口數:'))
womencount = int(input('請輸入女性人口數:'))

menlist = [i for i in range(mencount)]
womenlist = [i for i in range(womencount)]

menlist.reverse()
print(menlist)
print(womenlist)
marry = zip(menlist,womenlist)

for (mennum,wonum) in marry:
    print('結婚的男森:',mennum)
    print('結婚的女森:',wonum,'\n')
