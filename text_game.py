"""
This script is a simple text-based adventure game called "Treasure Hunt". The goal of the game is to find the hidden treasure by navigating through various locations. The treasure and locations are randomly generated from a predefined list.

Usage:

1. Run the script to start the game.
2. Follow the on-screen prompts to navigate through the locations using the commands: N (North), S (South), E (East), or W (West).
3. The game will continue until you find the hidden treasure in one of the locations.

How the game works:

The game begins with an introduction message explaining the objective and controls.
The treasure is hidden in one of the locations, except for the starting location, the 'Forest'.
The player starts in the 'Forest' and can navigate through different locations using the commands: N, S, E, or W.
The player's move will randomly take them to a new location.
The game continues until the player reaches the location where the treasure is hidden.

Example:
Welcome to the Treasure Hunt game!
...
You are currently in the Forest.
Enter your move (N, S, E, W): N
You've reached a new location, but the treasure is not here. Keep searching!

You are currently in the Dune.
Enter your move (N, S, E, W): E
...
Congratulations! You've found the treasure in the Sunken Temple!
"""

import random


def print_intro():
    print("Welcome to the Treasure Hunt game!")
    print("You are on a mission to find the hidden treasure.")
    print("Navigate through various locations to find the treasure.")
    print("You can move north, south, east, or west using the commands: N, S, E, W")
    print("Good luck adventurer!\n")


def get_random_location():
    locations = ['Forest', 'Cave', 'Desert', 'River', 'Mountain', 'Beach', 'Volcano', 'Swamp', 'Jungle', 'Tundra', 'Savannah', 'Canyon', 'Island', 'Oasis', 'Rainforest', 'Glacier', 'Meadow', 'Marsh', 'Wetland', 'Prairie', 'Steppe', 'Plateau', 'Valley', 'Hill', 'Dune', 'Gorge', 'Fjord', 'Cliff', 'Waterfall', 'Coral Reef', 'Icy Cave', 'Mangrove Forest', 'Haunted Mansion', 'Abandoned Mine', 'Ancient Ruins', 'Sunken Ship', 'Underground City', 'Secret Garden', 'Crystal Cavern', 'Lighthouse', 'Mausoleum', 'Astral Plane', 'Enchanted Forest', 'Floating Island', 'Lost City', 'Sky Castle', 'Mystic River', 'Fortress', 'Dungeon', 'Castle', 'Temple', 'Shrine', 'Oubliette', 'Observatory', 'Library', 'Marketplace', 'Tavern', 'Farm', 'Windmill', 'Graveyard', 'Battlefield', 'Colosseum', 'Throne Room', 'Alchemy Lab', 'Mage Tower', 'Training Ground', 'Bazaar', 'Monastery', 'Cathedral', 'Docks',
                 'Harbor', 'Lunar Landscape', 'Mushroom Forest', 'Petrified Forest', 'Clock Tower', 'City Square', 'Rooftops', 'Sewers', 'Underworld', 'Elemental Plane', 'Ethereal Plane', 'Pocket Dimension', 'Sanctuary', 'Hidden Valley', 'Mirage Village', 'Dragon\'s Lair', 'Necromancer\'s Crypt', 'Elven Grove', 'Dwarven Forge', 'Goblin Camp', 'Orchard', 'Vineyard', 'Giant\'s Table', 'Subterranean Lake', 'Cursed Island', 'Ghost Town', 'Wizard\'s Workshop', 'Invisible Maze', 'Amphitheater', 'Statue Garden', 'Museum', 'Treasure Vault', 'Royal Gardens', 'Grand Library', 'Undersea Palace', 'Sunken Temple', 'Great Wall', 'Pyramid', 'Sphinx', 'Ziggurat', 'Mausoleum of the Emperor', 'Ancient Observatory', 'Stone Circle', 'Ice Palace', 'Crystal Palace', 'Celestial Tower', 'Eternal Battlefield', 'Frozen Wasteland', 'Labyrinth', 'Hall of Mirrors', 'Endless Staircase', 'Timeless Void', 'Forbidden Zone']
    return random.choice(locations)


def get_treasure_location():
    treasure_location = get_random_location()
    while treasure_location == 'Forest':
        treasure_location = get_random_location()
    return treasure_location


def get_user_input():
    valid_input = ['N', 'S', 'E', 'W']
    user_input = input("Enter your move (N, S, E, W): ").upper()
    while user_input not in valid_input:
        user_input = input(
            "Invalid input. Please enter a valid move (N, S, E, W): ").upper()
    return user_input


def main():
    print_intro()

    treasure_location = get_treasure_location()
    current_location = 'Forest'

    while True:
        print(f"You are currently in the {current_location}.")

        user_move = get_user_input()
        current_location = get_random_location()

        if current_location == treasure_location:
            print(
                f"\nCongratulations! You've found the treasure in the {current_location}!")
            break
        else:
            print(
                f"You've reached a new location, but the treasure is not here. Keep searching!\n")


if __name__ == "__main__":
    main()
