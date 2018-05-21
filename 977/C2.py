#!/usr/bin/env python3

given = input()
integers = input()

given = given.split()
n = int(given[0])
k = int(given[1])

integers = integers.split()
sequence = [int(i) for i in integers]
sequence.sort()
if (k==0):
    if (sequence[0]==1):
        print("-1")
    else:
        print("1")
    exit(0)

if (k==n):
    print(sequence[k-1])
    exit(0)

m = sequence[k-1]
if ((k==1)and(n==1)):
    print(m)
    exit(0)
if (m==sequence[k]):
    print("-1")
else:
    print(m)
