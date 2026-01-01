#!/bin/python3

import math
import os
import random
import re
import sys


K = 1 # sort by Kth element
arr = [[10, 2, 5],[7, 1, 0],[9, 9, 9],[1, 23, 12],[6, 5, 9]]
result = sorted(arr, key = lambda r: r[K])
print(result)