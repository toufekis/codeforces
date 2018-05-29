#!/usr/bin/env python3

n = int(input())
l=list()
for i in range(n):
    word = input()
    if len(word)<=10:
        l.append(word)
    else:
        k = word[0]+str(len(word)-2)+word[-1]
        l.append(k)

for j in l:
    print(j)
