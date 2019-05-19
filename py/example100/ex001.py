#!/usr/bin/python
# -*- coding: UTF-8 -*-

for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if x != y and y != z and x != z:
                print(x, y, z)