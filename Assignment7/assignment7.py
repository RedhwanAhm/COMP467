# Redhwan Ahmed
# Assignment 7
# Professor Chaja - COMP 467

# Frames provided:
frames = [35, 1569, 14000, 955555]

# Loop that formats the frame numbers into seconds, then seconds and minutes, minutes and hours, and timecodes it.
for frame in frames:
    total_seconds = int(frame / 24.0)
    # Use divmod function to separate the whole number and remainder in the function into separate variables.
    minutes, seconds = divmod(total_seconds, 60) 
    hours, minutes = divmod(minutes, 60)
    # Then print the timecode per frame in frames creating an f string.
    timecode = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{frame % 24:02d}"
    print(f"{frame} is {timecode}")