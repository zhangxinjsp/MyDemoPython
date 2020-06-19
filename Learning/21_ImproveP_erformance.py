#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from numba import jit  # compiling Python code using LLVM


# @jit
def is_prime(i):
    for test in range(2, i):
        if i % test == 0:
            return False
    return True


# @jit
def tp():
    n_loops = 50000
    n_primes = 0

    for i in range(0, n_loops):
        if is_prime(i):
            n_primes += 1
    return n_primes


if __name__ == '__main__':
    t1 = time.time()

    n_primes = tp()

    t2 = time.time()
    print(str(n_primes))
    print("run time:%f s" % (t2 - t1))
