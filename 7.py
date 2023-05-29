a = [144, -14, 4, 85]
b = []
c = []
l = 0
maxP1 = 0
maxP2 = 0
maxN1 = 0
maxN2 = 0
amount = 0
minP = 100000
minN = 100000
n = len(a)
for i in range(n):
    if a[i] > 0:
        if a[i] < minP:
            minP = a[i]
        if abs(a[i]) > maxP2:
            if abs(a[i]) > maxP1:
                maxP2 = maxP1
                maxP1 = abs(a[i])
            else:
                maxP2 = abs(a[i])
            if(maxP2 != 0):
                for j in range(maxP1 - maxP2 - 1):
                    b.append(0)
            b.append(maxP1)
        else:
            b[a[i] - minP] = 1
    if a[i] < 0:
        amount += 1
        a[i] = abs(a[i])
        if a[i] < minN:
            minN = a[i]
        if abs(a[i]) > maxN2:
            if abs(a[i]) > maxN1:
                maxN2 = maxN1
                maxN1 = abs(a[i])
            else:
                maxN2 = abs(a[i])
            if(maxN2 != 0):
                for j in range(maxN1 - maxN2 - 1):
                    c.append(0)
            c.append(maxN1)
        else:
            c[a[i] - minN] = 1
if amount != 1:
    for i in range(len(c) - 1, 0, -1):
        if c[i] == 0:
            print(i - maxN1)
            l = 1
            if l == 1:
                break
    if l != 1:
        for i in range(maxP1):
            if b[i] == 0:
                print(i + minP)
                break
else:
    print('Минимальный пропущенный элемент:', -minN + 1)


