import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = sorted(input())
    from collections import Counter
    for k, v in Counter(s).most_common(3):
        print(k, v)

#company logo pypy3