"""Test_rotation_utils
Tali Berzins
To test the rotation_utils module
"""

import pytest
from rotation_utils import adjust_rotation

def test_rotation_numeric_inputs():
     assert adjust_rotation(100) == 100
     assert adjust_rotation(460) == 100
     assert adjust_rotation(820) == 100
     assert adjust_rotation(-100) == 260
     assert adjust_rotation(-460) == 260
     assert adjust_rotation(-820) == 260


def test_non_numeric():
     assert adjust_rotation("string") == 


