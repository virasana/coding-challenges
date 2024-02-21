#!/bin/python3

import math
import os
import random
import re
import sys


k = 1
arr = [[10, 2, 5],[7, 1, 0],[9, 9, 9],[1, 23, 12],[6, 5, 9]]
result = sorted(arr, key = lambda r: r[k])
print(result)