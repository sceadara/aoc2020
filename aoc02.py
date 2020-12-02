#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Advent of Code 2020 Coding Challenge

My solution for part 1 and 2 of day 2.
Lazy and stupid :) but got two stars with.
"""

__author__ = "Chris 'sceadara' Kirchmaier"
__copyright__ = "Copyright 2020, Nandecore"
__version__ = "1.0.0"
__email__ = "ck@nandecore.net"

with open('inputSources/aoc02.input') as input:
    validCount = 0
    validFalseCount = 0

    for line in input:
        line = line.strip()
        lineSplit = line.split(': ')
        policy = lineSplit[0]
        letter = policy[-1]
        minMax = policy[:-2].split('-')
        pwd = lineSplit[1]

        # PART 1
        count = 0
        for i in pwd:
            if i == letter:
                count += 1

        if int(minMax[0]) <= count <= int(minMax[1]):
            validFalseCount += 1

        # PART 2
        valid = True

        if pwd[int(minMax[0]) - 1] != letter != pwd[int(minMax[1]) - 1]:
            valid = False
        if pwd[int(minMax[0]) - 1] == letter == pwd[int(minMax[1]) - 1]:
            valid = False

        if valid:
            validCount += 1

    print('Old valid count: ', validFalseCount)
    print('New valid count: ', validCount)
