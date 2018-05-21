#!/usr/bin/env python3

number = input()
number = number.split()
n = int(number[0])
k = int(number[1])

while k>0:
    if (n%10)==0:
        n = n//10
    else:
        n-=1
    k-=1
print(n)
