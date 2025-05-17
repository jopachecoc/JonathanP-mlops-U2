import sys
import os
import pytest  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from diagnosticos import enfermedad1

def test_enfermedad():
  assert enfermedad1(110,79,90,37) == 'NO ENFERMO'
  assert enfermedad1(110,79,90,38) == 'ENFERMEDAD LEVE'
  assert enfermedad1(110,79,101,37) == 'ENFERMEDAD AGUDA'
  assert enfermedad1(121,79,90,37) == 'ENFERMEDAD CRÓNICA'
  assert enfermedad1(500,79,90,37) == 'ENFERMEDAD TERMINAL'

