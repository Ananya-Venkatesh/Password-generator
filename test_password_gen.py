# test_password_gen.py
import re, pytest
from password_gen import generate_password, PolicyError

def test_length_and_classes():
    p = generate_password(12)
    assert len(p) == 12
    assert any(c.islower() for c in p)
    assert any(c.isupper() for c in p)
    assert any(c.isdigit() for c in p)
    assert any(c in "!@#$%^&*()-_=+[]{};:,.?/" for c in p)

def test_exclusion_impossible():
    with pytest.raises(PolicyError):
        # exclude every lowercase letter but still require 'lower'
        generate_password(8, require_classes=("lower",), exclude_chars="abcdefghijklmnopqrstuvwxyz")

def test_no_adjacent_repeat():
    p = generate_password(200, no_repeat=True)
    assert all(p[i] != p[i+1] for i in range(len(p)-1))
