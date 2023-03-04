from project import get_player_names
from project import welc_msg
from project import get_dice_value
from project import bitten
from project import ladder
from project import snake_ladder_actions
from project import check_win
import pytest
from unittest.mock import patch

def main():
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

if __name__ == "__main__":
    main()
