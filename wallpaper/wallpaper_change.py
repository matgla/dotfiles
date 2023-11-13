#!/bin/python3

import argparse 
import os 
import random
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser("Script to change wallpapers")
parser.add_argument("--input", "-i", help="Path to wallpapers directory", required=True)

args, _ = parser.parse_known_args()

wallpaper = random.choice(os.listdir(args.input))

path = (Path(args.input) / wallpaper).absolute()
subprocess.run("swww img " + str(path) + " --transition-step 200 --transition-fps 50 --transition-type center", shell=True)

subprocess.run("wal -c", shell=True)
subprocess.run("wal -b '#000000' --cols16 --backend schemer2 --saturate 1.0  -i " + str(path), shell=True)
subprocess.run("eww reload", shell=True)
