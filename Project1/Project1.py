# Redhwan Ahmed
# Project 1
# Professor Chaja - COMP 467


import argparse
import sys

#Parse arguments for job
parser = argparse.ArgumentParser()
parser.add_argument("--job", dest="jobFolder", help="job to process")
parser.add_argument("--verbose", action="store_true", help="show verbose")
parser.add_argument("--TC", dest="timecode", help="Timecode to process")

args = parser.parse_args()

if args.jobFolder is None:
    print("No job selected")
    sys.exit(2)
else:
    job = args.jobFolder

if args.timecode:
    timecodeTC = args.timecode

