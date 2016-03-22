#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from random import random


def reservoir(iterator, K):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len(result) < K:
            result.append(item)
            logging.warn('Adding %r to unfilled reservoir', item)
        else:
            ind = int(random() * N)
            if ind < K:
                logging.warn('Probability %s/%s: replacing item %s with %r',
                             K, N, ind, item)
                result[ind] = item

    return result


if __name__ == '__main__':
    import sys
    sample = reservoir(sys.stdin, int(sys.argv[1]))
    for row in sample:
        print(row.rstrip())