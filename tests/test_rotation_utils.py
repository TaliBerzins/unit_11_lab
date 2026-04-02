"""Test_rotation_utils
Tali Berzins
To test the rotation_utils module
"""

import pytest
from rotation_utils import adjust_rotation

def test_rotation_100():
    value = adjust_rotation(100)
    assert value == 100


