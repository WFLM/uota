from uota import *

def test_normalize_version():
    nv = normalize_version
    assert nv("0.0.10") > nv("0.0.9")
    assert nv("0.2.1") > nv("0.2")
    assert nv("0.3") > nv("0.2.1")
