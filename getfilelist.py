#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os

def getList():
    files = os.listdir('./testdata')

    for item in files:
        print(item)

    return files
