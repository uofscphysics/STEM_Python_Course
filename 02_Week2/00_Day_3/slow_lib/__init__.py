import numpy as np
import time
import hashlib


def slow_random(val):
    val = str(val).encode()
    np.random.seed(seed=len(val))
    rand = np.random.normal(loc=0.0, scale=1.0)
    time.sleep(np.abs(rand))
    return hashlib.md5(val).hexdigest()


def fast_random(val):
    val = str(val).encode()
    return hashlib.md5(val).hexdigest()
