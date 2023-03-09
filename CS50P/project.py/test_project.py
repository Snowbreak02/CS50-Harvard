from project import get_player_names, welc_msg, get_dice_value, bitten, ladder, snake_ladder_actions, check_win
import pytest
from unittest.mock import patch
test_parameters = [
                    ("Alan\nJack\n", "\n'Alan' and 'Jack' will be playing against each other!⚔️\n"),
                    ("Mary\nMary\n", "\n'Mary' and 'Mary' will be playing against each other!⚔️\n"),
                    ("12345\nJenny\n", "\n'12345' and 'Jenny' will be playing against each other!⚔️\n")
                ]

@pytest.mark.parametrize("user_input, expected_output", test_parameters)
def test_get_player_names(user_input, expected_output, capfd):
    # Simulating user input
    with patch('builtins.input', side_effect=user_input.split('\n')):
        # Call the function
        get_player_names()

    # Capturing user output
    captured = capfd.readouterr()
    assert captured.out == expected_output

def test_welc_msg():
    ...

def test_get_dice_value():
    ...

def test_bitten():
    ...

def test_ladder():
    ...

def test_snake_ladder_actions():
    ...

def test_check_win():
    ...
