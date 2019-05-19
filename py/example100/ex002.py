#!/usr/bin/python
# -*- coding: UTF-8 -*-

while (True):
    s = input('净利润(q for exit):')
    if s.lower() == "q":
        break

    i = int(s)
    r = 0

    # arr = [1000000, 600000, 400000, 200000, 100000, 0]
    # rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

    # for idx in range(0, 6):
    #     if i > arr[idx]:
    #         r += (i - arr[idx]) * rat[idx]
    #         print((i - arr[idx]) * rat[idx])
    #         i = arr[idx]

    mix = ((1000000, .01), (600000, .015), (400000, .03), (200000, .05),
           (100000, .075), (0, .1))

    for rate in mix:
        if i > rate[0]:
            margin = (i - rate[0]) * rate[1]
            r += margin
            print(margin)

            i = rate[0]

    print(r)
