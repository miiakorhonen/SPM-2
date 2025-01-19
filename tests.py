from unittest.mock import patch, mock_open
from SPM2 import kysy_luku, hae_lomakkeesta

@patch('builtins.input', side_effect=['25'])
def test_valid_input(mock_input):
    assert kysy_luku() == 25

@patch('builtins.input', side_effect=['5'])
def test_below_range(mock_input):
    assert kysy_luku() is None

@patch('builtins.input', side_effect=['45'])
def test_above_range(mock_input):
    assert kysy_luku() is None

@patch('builtins.input', side_effect=['invalid'])
def test_invalid_input(mock_input):
    with patch('builtins.print') as mock_print:
        assert kysy_luku() is None
        mock_print.assert_called_with("Arvon tulee olla kokonaisluku.")

def test_kodin_lomake_valid_input_returns_correct_values():
    assert hae_lomakkeesta("lapsi", "kodin lomake", "näkö", 10) == ("40", "16")

def test_kodin_lomake_input_out_of_range_returns_none():
    assert hae_lomakkeesta("lapsi", "kodin lomake", "näkö", 50) is None

def test_koulun_lomake_valid_input_returns_correct_values():
    assert hae_lomakkeesta("lapsi", "koulun lomake", "SOC", 15) == ("51", "54")

def test_koulun_lomake_input_out_of_range_returns_none():
    assert hae_lomakkeesta("lapsi", "koulun lomake", "SOC", 5) is None