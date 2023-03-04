from project import get_player_names
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
