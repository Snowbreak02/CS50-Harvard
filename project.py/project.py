def main():
    welc_msg()
    time.sleep(actions_delay)
    p1_name, p2_name = get_player_nmes()
    time.sleep(actions_delay)

    p1_current_pos = 0
    p2_current_pos = 0

    while True:
        time.sleep(actions_delay)
        input_1 = input("\n" + p1_name + ": " + random.choice(txt_for_plyr_turn))
        print("\n..🎲🎲..Dice is being rolled..🎲🎲..")
        dice_val = get_dice_value()
        time.sleep(actions_delay)
        print(p1_name + "is moving...")
        p1_current_pos = snake_ladder(p1_name, p1_current_pos, dice_value)
        



def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()