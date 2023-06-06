import random

def roll_dice(num_dice, dice_type):
    results = []
    for _ in range(num_dice):
        result = random.randint(1, dice_type)
        results.append(result)
    return results
