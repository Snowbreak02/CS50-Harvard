# My own Snake and Ladder Game!!

import time
import random
import sys

def main():
    welc_msg()
    time.sleep(actions_delay)
    p1_name, p2_name = get_player_nmes()
    time.sleep(actions_delay)

    p1_current_pos = 0
    p2_current_pos = 0

    while True:
        time.sleep(actions_delay)
        input_1 = input("\n" + p1_name + ": " + random.choice(txt_for_plyr_turn) + "Press enter to roll the 🎲dice🎲: ")
        print("\n..🎲🎲..Dice is being rolled..🎲🎲..")
        dice_val = get_dice_value()
        time.sleep(actions_delay)
        print(p1_name + "is moving...")
        p1_current_pos = snake_ladder(p1_name, p1_current_pos, dice_value)

        check_win(p1_name, p1_current_pos)

        input_2 = input("\n" + p2_name + ": " + random.choice(txt_for_plyr_turn) + "Press enter to roll the 🎲dice🎲: ")
        print("\n..🎲🎲..Dice is being rolled..🎲🎲..")
        dice_val = get_dice_value()
        time.sleep(actions_delay)
        print(p2_name + "is moving...")
        p2_current_pos = snake_ladder(p2_name, p2_current_pos, dice_value)

        check_win(p2_name, p2_current_pos)


def welc_msg():
    print("Hi there, Welcome to my very first game of Snakes and Ladders, created using Python!")
    print("This is a 2 player game where each player will take turns rolling the dice and advancing till one reaches 70. May the luckiest player win!🏆")

actions_delay = 1
MAX_VAL = 70
DICE_FACE = 6

def get_player_names():
    p1_name = None
    while not in p1_name:
        p1_name = input("Name of first player: ").strip()

    p2_name = None
    while not in p2_name:
        p2_name = input("Name of second player: ").strip()

    print(f"\n'{p1_name}' and '{p2_name}' will be playing against each other!⚔️")
    return p1_name, p2_name

def get_dice_value():
    time.sleep(actions_delay)
    dice_value = random.randint(1, DICE_FACE)
    print("Dice value: " + str(dice_value))
    return dice_value

def bitten(old_value, current_value, player_name):
    print("\n" + random.choice(text_for_snake_bite).upper() + "🐍🐍🐍🐍🐍")
    print("\n"" " + player_name + " has been bitten by a snake! Going down from " + str(old_value) + " to " + str(current_value))

def ladder(old_value, current_value, player_name):
    print("\n" + random.choice(text_for_ladder_jump).upper() + "⬆️ 🔥📈🔥📈⬆️")
    print("\n" + player_name + " is climbing the ladder from " + str(old_value) + " to " + str(current_value))

def snake_ladder_actions(dice_value, current_value, player_name):
    time.sleep(actions_delay)
    old_value = current_value
    current_value = current_value + dice_value

    if current value < MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print(f"\n{player_name} moved from {old_value} to {current_value}")

    if current_value in snake_position:
        final_value = snake_position.get(current_value)
        bitten(current_value, final_value, player_name)

    elif current_value in ladders_position:
        final_value = ladders_position.get(current_value)
        ladder(current_value, final_value, player_name)






if __name__ == "__main__":
    main()