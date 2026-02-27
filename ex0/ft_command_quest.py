#!/usr/bin/env python3
import sys

print("=== Command Quest ===")
args = sys.argv
if len(args) < 2:
    print("No arguments provided!")
    print(f"Program name: {args[0]}")
else:
    print(f"Program name: {args[0]}")
    print(f"Arguments received: {len(args)-1}")
    for i, arg in enumerate(args[1:], 1):
        print(f"Argument {i}: {arg}")

print(f"Total arguments: {len(args)}\n")
