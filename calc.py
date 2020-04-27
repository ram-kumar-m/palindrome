import time
import math
import sys

sys.setrecursionlimit(999999999)


def palindrome(s: str):
    rev_s = s[::-1]
    print(s, ' ', rev_s)
    if s == rev_s:
        print(s)
        with open('./output', 'w') as f:
            f.write(s)

    else:
        s = str(int(s)+int(rev_s))
        with open('./temp','a') as f:
            f.write(s+'\n')
        return palindrome(s)


palindrome('189')
