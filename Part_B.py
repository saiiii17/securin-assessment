from collections import Counter
import itertools

def roll_distribution(dice1, dice2):
    distribution = Counter()
    for face1 in dice1:
        for face2 in dice2:
            distribution[face1 + face2] += 1
    return distribution

def main():
    target_distribution = Counter({
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    })
    
    
    dice1_face_values = range(1, 5)  # limiting dice1 to values 1, 2, 3, and 4
    dice2_face_values = range(1, 9)  # keeping dice2 within the range 1 to 8

    # Generate all possible dice combinations within the specified ranges
    possible_dice1 = list(itertools.combinations_with_replacement(dice1_face_values, 6))
    possible_dice2 = list(itertools.combinations_with_replacement(dice2_face_values, 6))

    # Find all pairs of dice that match the target distribution
    matching_pairs = []
    for dice1 in possible_dice1:
        for dice2 in possible_dice2:
            if roll_distribution(dice1, dice2) == target_distribution:
                matching_pairs.append((dice1, dice2))

    
    print("Matching pairs of dice:")
    for dice1, dice2 in matching_pairs:
        print(f"Dice 1: {dice1}, Dice 2: {dice2}")

if __name__ == "__main__":
    main()
