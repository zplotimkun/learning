userinput = input('輸入一串字:')

listinput = list(userinput)

strlist = []
longstrlist = []
for i in range(len(listinput)):
    for j in range(i,len(listinput)):
        if listinput[j] in strlist:
            longstrlist.append("".join(strlist))
            strlist.clear()
            break
        else:
            strlist.append(listinput[j])

print('最長字串:',max(longstrlist, key=len))
print('字數:',len(max(longstrlist, key=len)))
