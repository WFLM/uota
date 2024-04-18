"""
Testing suite for uota.

Written using raw MicroPython code, not depending on any testing framework.
Suited to be copy/pasted into MicroPython REPL on a microcontroller to run all tests.

MIT license; Copyright (c) 2024 Martin Komon
"""

from uota import *

# test definitions

def test_normalize_version():
    nv = normalize_version
    assert nv("0.0.10") > nv("0.0.9")
    assert nv("0.2.1") > nv("0.2")
    assert nv("0.3") > nv("0.2.1")
    assert nv("0.3.0") > nv("0.3")  # more specific > general == true, I guess
    print("normalize_version ok")


# test execution
test_normalize_version()
