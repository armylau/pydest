from mss import mss

# start capture screen using mss lib

# The simplest use, save a screen shot of the 1st monitor
with mss() as sct:
    filename = sct.shot(mon=-1, output='fullscreen.png')
    print(filename)

for filename in sct.save():
    print(filename)

