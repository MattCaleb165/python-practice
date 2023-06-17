import random

def roll_dice(num_dice, dice_type):
    if dice_type == "6-sided":
        dice_range = 6
    elif dice_type == "4-sided":
        dice_range = 4
    else:
        raise ValueError("Invalid dice type")

    results = []
    for _ in range(num_dice):
        result = random.randint(1, dice_range)
        results.append(result)

    return results

