# Redhwan Ahmed
# Assignment 9
# Professor Chaja - COMP 467

import subprocess

# Command 1: Extract frames from the video at a rate of 1 frame per second
subprocess.run(["ffmpeg", "-i", "input.mp4", "-vf", "fps=1", "frames/%04d.jpg"])

# Command 2: Convert the video to a different format
subprocess.run(["ffmpeg", "-i", "input.mp4", "-c:v", "libx264", "-c:a", "copy", "output.mov"])
