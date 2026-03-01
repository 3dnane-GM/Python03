#!/usr/bin/env python3

achievements = {
    "alice": [
        "first_blood",
        "pixel_perfect",
        "speed_runner",
        "first_blood",
        "first_blood",
    ],
    "bob": [
        "level_master",
        "boss_hunter",
        "treasure_seeker",
        "level_master",
        "level_master",
        "first_blood",
    ],
    "charlie": [
        "treasure_seeker",
        "boss_hunter",
        "combo_king",
        "first_blood",
        "boss_hunter",
        "first_blood",
        "boss_hunter",
        "first_blood",
    ],
    "diana": [
        "first_blood",
        "combo_king",
        "level_master",
        "treasure_seeker",
        "speed_runner",
        "combo_king",
        "combo_king",
        "level_master",
    ],
    "eve": [
        "level_master",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
    ],
    "frank": [
        "explorer",
        "boss_hunter",
        "first_blood",
        "explorer",
        "first_blood",
        "boss_hunter",
    ],
    "IceWard": [
        "boss_hunter",
        "first_blood",
        "first_blood",
        "boss_hunter",
        "The Honored One"
    ],
}


def main():
    """function to rub the main program"""
    print("=== Achievement Tracker System ===\n")

    for name, milestone in achievements.items():
        print(f"Player {name} achievements:", set(milestone))

    print()

    all_achievements = [set(achievements[name]) for name in achievements]

    print("=== Achievement Analytics ===")

    unique_achievements = set.union(*all_achievements)
    if len(unique_achievements) == 0:
        unique_achievements = None
    print("All unique achievements:", unique_achievements)
    print("Total unique achievements:", len(unique_achievements))
    print()

    common_achievements = set.intersection(*all_achievements)
    if len(common_achievements) == 0:
        common_achievements = None
    print("Common to all players:", common_achievements)

    rare_achievement = set()
    for i, player in enumerate(all_achievements):
        others_union = set().union(*[all_achievements[j] for j
                                     in range(len(all_achievements))
                                     if j != i])
        rare_achievement |= player.difference(others_union)

    print("Rare achievements (1 player):", rare_achievement)
    print()

    alice = set(achievements["alice"])
    bob = set(achievements["bob"])
    IceWard = set(achievements["IceWard"])
    print("Alice vs Bob common:", alice.intersection(bob))
    print("Alice unique:", alice.difference(*all_achievements[1:]))
    print("IceWard unique:", IceWard.difference(*all_achievements[:5]))


if __name__ == "__main__":
    main()
