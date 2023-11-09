#!/bin/python3

import alsaaudio
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--icon", action="store_true")
parser.add_argument("--value", action="store_true")

args, _ = parser.parse_known_args()

m = alsaaudio.Mixer()
v = int(m.getvolume()[0])

if args.icon:
    if int(m.getmute()[0]) == 1:
        print("󰝟")
    else:
        if v < 30:
            print("")
        elif v > 30 and v < 70:
            print("")
        else:
            print("")

if args.value:
    print(str(v) + "%")
