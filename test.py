import numpy as np
import pytest
def inc(x):
  return x + 1
def test_inc():
  assert inc(3) == 4
