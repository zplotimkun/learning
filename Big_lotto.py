import random
from collections import Counter

lottornum = list()
luckynum = list()

lottornum = [i for i in range(1,43)]

luckynum = random.sample(lottornum,7)
        
specialnum = luckynum[6:7]
print (luckynum)
print ('普通號: ',luckynum[0:6])
print ('特別號: ',specialnum)


usernum = list()

while len(usernum) < 6:
    try:
        num = int(input('請輸入第 {count} 個數字'.format(count=len(usernum)+1)))
        
        if (num not in range(1, 43) or num in usernum):
            raise Exception('輸入不正確')
        usernum.append(num)
    except Exception as e:
        print(str(e))

print('選擇號碼: ',usernum)



x = set(luckynum[0:6])
y = set(usernum)

bingo= x & y
bingosp = y & set(specialnum)

if(len(bingo) > 0):
    print('你的中獎號碼',sorted(bingo),'號碼')
    if(len(bingosp) > 0):
        print('還中了特別號')
    else:
        print('你沒有中特別號')
else:
    print('你沒有中獎')
