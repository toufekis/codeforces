#!/usr/bin/env python3

import sys

rows = int(input())
if rows < 1 or rows > 1000:
    sys.exit()
seats = list()
correct1 = ["OO|OO", "OO|OX", "OO|XO", "OO|XX"]
correct2 = ["OX|OO", "OX|OX", "OX|XO", "OX|XX"]
correct3 = ["XO|OO", "XO|OX", "XO|XO", "XO|XX"]
correct4 = ["XX|OO", "XX|OX", "XX|XO", "XX|XX"]
correct = correct1 + correct2 + correct3 + correct4
for i in range(rows):
    pairs = input()
    if pairs not in correct:
        sys.exit()
    seats.append(pairs)
seat = ""
for j in seats:
    seat += j+"?"

empty = seat.find("OO")

if empty != -1:
    seat = seat.replace("OO", "++", 1)
    newseats = seat.split(sep="?")
    print("YES")
    for newseat in newseats:
        print(newseat)
else:
    print("NO")
