#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 Coding Challenge

My solution for part 1 and 2 of day 1.
Lazy and stupid :) but got two stars with.
"""

__author__ = "Chris 'sceadara' Kirchmaier"
__copyright__ = "Copyright 2020, Nandecore"
__version__ = "1.0.0"
__email__ = "ck@nandecore.net"

with open('inputSources/aoc01.input') as input:

    numbers = list(map(int, input))

    # PART 1
    for i in numbers:
        for y in numbers:
            if i+y == 2020:
                print(i*y)

    # PART 2
    for i in numbers:
        for y in numbers:
            for e in numbers:
                if i+y+e == 2020:
                    print(i*y*e)
