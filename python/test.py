#!/usr/bin/env python
import random

from lcs import lcs


def main():
    LEN = 60
    a = ''.join(random.choice(('a', 'c', 'g', 't')) for i in xrange(LEN))
    b = ''.join(random.choice(('a', 'c', 'g', 't')) for i in xrange(LEN))
    print lcs(a, b, 3, True)


if __name__ == '__main__':
    main()
