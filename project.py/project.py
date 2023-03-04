# My own Snakes and Ladders Game using Python!!

import time
import random
import sys

def main():
    welc_msg()
    time.sleep(actions_delay)
    p1_name, p2_name = get_player_names()
    time.sleep(actions_delay)

    p1_current_pos = 0
    p2_current_pos = 0

    while True:
        time.sleep(actions_delay)
        input_1 = input("\n" + p1_name + ": " + random.choice(txt_for_plyr_turn) + " Press enter to roll the 🎲dice🎲: ")
        print("\n..🎲🎲..Dice is being rolled..🎲🎲..")
        dice_value = get_dice_value()
        time.sleep(actions_delay)
        print(p1_name + " is moving...", end="" )
        p1_current_pos = snake_ladder_actions(p1_name, p1_current_pos, dice_value)

        check_win(p1_name, p1_current_pos)

        input_2 = input("\n" + p2_name + ": " + random.choice(txt_for_plyr_turn) + " Press enter to roll the 🎲dice🎲: ")
        print("\n..🎲🎲..Dice is being rolled..🎲🎲..")
        dice_value = get_dice_value()
        time.sleep(actions_delay)
        print(p2_name + " is moving...")
        p2_current_pos = snake_ladder_actions(p2_name, p2_current_pos, dice_value)

        check_win(p2_name, p2_current_pos)


def welc_msg():
    print("Hi there! Welcome to my very first game of Snakes and Ladders created using Python!")
    print("This is a 2 player game where each player will take turns rolling the dice and advancing till one reaches 70.\n🏆May the luckiest player win!🏆")

actions_delay = 1
MAX_VAL = 70
DICE_FACE = 6

def get_player_names():
    while True:
            p1_name = input("\nName of first player: ").title()
            if p1_name.isalpha():
                break
            else:
                print("Please use only letters, try again")

    while True:
            p2_name = input("\nName of second player: ").title()
            if p2_name.isalpha() and p2_name != p1_name:
                break
            if p2_name == p1_name:
                print("Please do not use the same names!")
            else:
                print("Please use only letters, try again")

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
    if current_value < MAX_VAL:
      print("You now need " + str(MAX_VAL - current_value) + " to win this game. Keep going.")

def ladder(old_value, current_value, player_name):
    print("\n" + random.choice(text_for_ladder_jump).upper() + "⬆️ 🔥📈🔥📈⬆️")
    print("\n" + player_name + " is climbing the ladder from " + str(old_value) + " to " + str(current_value))
    if current_value < MAX_VAL:
      print("You now need " + str(MAX_VAL - current_value) + " to win this game. Keep going.")


def snake_ladder_actions(player_name, current_value, dice_value):
    time.sleep(actions_delay)
    old_value = current_value
    current_value = current_value + dice_value

    print(f"{player_name} moved from {old_value} to {current_value}")

    if current_value in snake_position:
        final_value = snake_position.get(current_value)
        bitten(current_value, final_value, player_name)

    elif current_value in ladders_position:
        final_value = ladders_position.get(current_value)
        ladder(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

def check_win(player_name, position):
    time.sleep(actions_delay)
    if MAX_VAL <= position:
        print(f"\n🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊🎊 '{player_name}' HAS WON THE GAME!!🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉\n")
        sys.exit(1)

txt_for_plyr_turn = [
    "Its your turn.",
    "Are you prepared?",
    "Feeling lucky?",
    "Time waits for no man.",
    "You're doing great.",
    "Ready to be a champion?"
]

text_for_snake_bite = [
    "oh no...",
    "OUCH!",
    "OOF!",
    "oops...",
    "DANG!",
    "CHOMP!"
]

text_for_ladder_jump = [
    "Yipee!",
    "YAHoo!",
    "hurrayyy!",
    "oh my Goodness...",
    "On fire🔥🔥",
    "You are a champion.",
    "Winning this already?!"
]

snake_position = {
    12: 4,
    16: 6,
    19: 9,
    22: 11,
    28: 14,
    37: 7,
    42: 8,
    53: 31,
    59: 27,
    63: 47,
    69: 36,
}

ladders_position = {
    3: 26,
    5: 15,
    10: 20,
    13: 44,
    21: 41,
    25: 51,
    29: 49,
    36: 57,
    48: 60,
    43: 66,
}



if __name__ == "__main__":
    main()