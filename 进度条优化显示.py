# -*- coding: utf-8 -*-
"""
@Time:   2021/3/1 14:11
@Author: Hudaiguo
@python version: 3.5.2
"""

from tqdm import trange
from tqdm import tqdm
import time

for i in trange(100):
    time.sleep(0.01)

for it in tqdm(range(10)):
    time.sleep(0.5)

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    time.sleep(0.25)
    text = text + char

print(text)