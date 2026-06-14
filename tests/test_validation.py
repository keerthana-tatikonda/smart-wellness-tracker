# tests/test_validation.py
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from validation import (
    validate_name,
    validate_stress,
    validate_energy
)


def test_valid_name():
    assert validate_name("Keerthana") == True


def test_blank_name():
    assert validate_name("") == False


def test_valid_stress():
    assert validate_stress(5) == True


def test_invalid_stress_high():
    assert validate_stress(15) == False


def test_invalid_stress_low():
    assert validate_stress(0) == False


def test_valid_energy():
    assert validate_energy(8) == True


def test_invalid_energy():
    assert validate_energy(20) == False