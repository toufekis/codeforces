#!/usr/bin/env python3

n = int(input())
line = list(input())
l = list()
k = list()

for i in range(n-1):
    l.append(line[i]+line[i+1])

for m in range(len(l)):
    k.append(0)



for j in range(len(l)):
    count = 0
    for v in range(len(l)):
        if (l[j]==l[v]):
            count+=1
            k[j]=count

max_value = max(k)
max_index = k.index(max_value)

print(l[max_index])
