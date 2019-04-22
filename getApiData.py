#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

print("content-type:text/html; charset=utf-8\n")  # headers
print()

import os
import pandas as pd

files = os.listdir('./testdata')

for item in files:
    print(item)
    subfiles = os.listdir('./testdata/' + files[item])
    print(subfiles)

    # data = pd.read_csv("./data/rawdata_v190406/")

