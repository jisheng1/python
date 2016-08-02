# -*- coding:utf-8 -*-

def triangles():
   yield [1]
   L = [1,1]
   while True :
        yield L
        #H = L
        H = [x for x in L]
        for x in range(1,len(L)) :
            L[x] = H[x-1] + H[x]
        L.append(1)


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
