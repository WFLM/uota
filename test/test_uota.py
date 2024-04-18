"""
testing suite for uota

written using raw MicroPython code, not depending on any testing framework
suited to be copy/pasted into MicroPython REPL on a microcontroller to run all tests

"""

from uota import *

# test definitions

def test_normalize_version():
    nv = normalize_version
    assert nv("0.0.10") > nv("0.0.9")
    assert nv("0.2.1") > nv("0.2")
    assert nv("0.3") > nv("0.2.1")
    print("normalize_version ok")


# test execution
test_normalize_version()
