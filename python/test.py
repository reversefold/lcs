#!/usr/bin/env python
import random

from lcs import lcs_string


def main():
    LEN = 60
    a = ''.join(random.choice(('a', 'c', 'g', 't')) for i in range(LEN))
    b = ''.join(random.choice(('a', 'c', 'g', 't')) for i in range(LEN))
    print(lcs_string(a, b, 3, True))


if __name__ == '__main__':
    main()
