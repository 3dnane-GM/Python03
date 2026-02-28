#!/usr/bin/env python3

import math
import sys

print("=== Game Coordinate System ===\n")
if len(sys.argv) < 2:
    coords1 = 0, 0, 0
    x1, y1, z1 = coords1
    nonparsed = "10, 20, 5"
    coords2 = tuple(int(p) for p in nonparsed.split(','))
    print(f"Position created: {coords2}")
    x2, y2, z2 = coords2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {coords1} and {coords2}: {distance:.2f}")
    print()

    nonparsed = "3,4,0"
    print(f"Parsing coordinates: \"{nonparsed}\"")
    coords2 = tuple(int(p) for p in nonparsed.split(','))
    print(f"Position created: {coords2}")
    x2, y2, z2 = coords2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {coords1} and {coords2}: {distance:.1f}")
    print()

    nonparsed = "abc,def,ghi"
    print(f"Parsing invalid coordinates \"{nonparsed}\"")
    try:
        coords2 = tuple(int(p) for p in nonparsed.split(','))
        print(f"Position created: {coords2}")
        x2, y2, z2 = coords2
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(f"Distance between {coords1} and {coords2}: {distance:.1f}")
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: ValueError, Args: (\"{e}\"),")

    print()
    print("Unpacking demonstration:\n"
          "Player at x=3, y=4, z=0\n"
          "Coordinates: X=3, Y=4, Z=0")

elif len(sys.argv) > 2:
    print("Wrong argument input format. Usage: "
          "python3 ft_coordinate_system.py \"x, y, z\"")

else:
    try:
        coords1 = 0, 0, 0
        x1, y1, z1 = coords1
        coords2 = tuple(int(p) for p in sys.argv[1].split(','))
        print(f"Parsing coordinates: \"{sys.argv[1]}\"")
        print(f"Position created: {coords2}")
        x2, y2, z2 = coords2
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(f"Distance between {coords1} and {coords2}: {distance:.1f}")
        print()
    except ValueError as e:
        print(f"Parsing invalid coordinates \"{sys.argv[1]}\"")
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: ValueError, Args: (\"{e}\"),")
