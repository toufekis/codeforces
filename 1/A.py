#!/usr/bin/env python3

import math, sys

# n=mhkos m=platos a=plakes
k = input()
k = k.split()
n = float(k[0])
m = float(k[1])
a = float(k[2])

if (n and m and a) < 1 or (n and m and a) > 10**9:
    sys.exit()

mhkos = math.ceil(n/a)
platos = math.ceil(m/a)
plakes = int(mhkos*platos)
print(plakes)
