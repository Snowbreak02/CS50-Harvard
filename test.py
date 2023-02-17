def generate_integer(level):
    if level == "1" or "2" or "3":
        count = 0
        score = 0
        while True:
            while True:
                try:
                    x = random.randint(0,10)
                    y = random.randint(0,10)
                    print(f"{x} + {y} = ", end="")
                    result = x + y
                    answer = int(input())
                    if answer == result:
                        score += 1
                        continue
                    elif answer != result:
                        count += 1
                        print("EEE")
                        continue
                except ValueError:
                    count += 1
                    print("EEE")
                    break
            if count == 3:
                    break

    return score