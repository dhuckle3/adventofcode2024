import sys
import os
import shutil

if len(sys.argv) != 2:
    print("Usage: python my_script.py [day01]")
    sys.exit(1)

name = sys.argv[1]
os.makedirs(f"aoc24/{name}")
os.makedirs(f"data/{name}")
shutil.copy("scripts/template.py", f"aoc24/{name}/{name}.py")
