food = input("Item: ")
food = food.lowercase()

match food:
    case "apple":
        print("Calories: 130")
    case "avocado"|"cantaloupe"|"honeydew melon"|"pineapple"|"strawberries"|"tangerine":
        print("Calories: 50")
    case "banana":
        print("Calories: 110")
    case "grapefruit"|"nectarine"|"peach":
        print("Calories: 60")
    case "grapes"|"kiwifruit":
        print("Calories: 90")
    case "lemon":
        print("Calories: 15")
    case "lime":
        print("Calories: 20")
    case "orange"|"watermelon":
        print("Calories: 80")
    case "pear"|"sweet cherries":
        print("Calories: 100")
    