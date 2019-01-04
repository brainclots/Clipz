#!/usr/local/bin/python3
import glob
import random
import os
import datetime
import time
import sys
from pathlib import Path
import platform

def get_it():
    global all_filenames
    # Determine OS we are running on
    OS = platform.system()
    # Get the list of files
    google_drive = os.environ['GDRIVE']
    google_drive = Path(google_drive)
    target_dir = google_drive / 'Music/Soundz/Clipz'
    listofiles = target_dir / 'listofiles.tmp'
    if listofiles.is_file():
        with open(listofiles) as f:
            all_filenames = f.read().splitlines()
    if len(all_filenames) == 0:
        wav_filenames = glob.glob(target_dir + '/*.wav')
        mp3_filenames = glob.glob(target_dir + '/*.mp3')
        all_filenames = wav_filenames + mp3_filenames
    # Shuffle the list and pick the 'lucky_one'
    random.shuffle(all_filenames)
    lucky_one = all_filenames.pop().strip()
    word_file = Path(lucky_one + ".txt")
    # Write newly shuffled list of files back to list (without the 'lucky_one')
    with open(listofiles, 'w') as f:
        for item in all_filenames:
            if item:
                f.write(f'{item}\n')

    # Get the words from the word_file
    if os.path.isfile(word_file):
        clip_file = open(word_file, 'r')
    else:
        clip_file_path = target_dir + '/snarky.txt'
        clip_file = open(clip_file_path, 'r')

    clip_txt = clip_file.read()
    num_lines = clip_txt.count('\n')
    clip_file.close()

    # The height of the window should be 29 lines from the shark plus however
    # many lines were in the word_file
    window_height = 29 + num_lines
    # Set window size to the right height in lines and 120 characters wide
    if OS == 'Windows':
        os.system(f'mode con: cols=120 lines={window_height}') # Windows
        os.system('color 3f') # Windows
    else:
        os.system('printf \033[8\;%d\;120t' % window_height) # Mac/Linux
        os.system('tput clear') # Mac/Linux
    # Show the top of the bubble
    print(" __________________  ")
    print("/                  \ ")
    # Show the contents of the words text file
    print(clip_txt, end="")
    shark = open(target_dir / 'snarkshark_short.txt', 'r')
    shark_txt = shark.read()
    shark.close()
    print(shark_txt, end=" ")
    # Show the name of the file being played
    lucky_parens = '( ' + os.path.basename(lucky_one) + ' )'
    print(f'{" ":75}{lucky_parens:^20}')
    # Set the title and play the sound
    if OS == 'Windows':
        os.system(f'title Playing {os.path.basename(lucky_one)}') # Windows
        os.system(f'swavplayer "{lucky_one}"') # Windows
    else: # Mac/Linux
        os.system(f'afplay -v .2 {lucky_one}')
        os.system('printf \033[8\;30\;120t')
        os.system('ttytle')
        os.system('tput clear')
    # Run the function to log what was played and when
    track_it(all_filenames, lucky_one)


def track_it(all_filenames, lucky_one):
    # Keep track for statistics
    with open('eightball.log', 'a') as f:
        # Get the date and time in proper format
        now = datetime.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')
        # Add the line to the log
        f.write(f'{now},{os.path.basename(lucky_one)}\n')
    # If running in a loop, pick a number between 15 and 120 seconds to wait
    if len(sys.argv) > 1:
        nap_length = random.randrange(15, 120)
        rest_it(nap_length)


def rest_it(nap_length, now=datetime.datetime.now):
    # 'try' block is to allow for a clean exit if pressing Ctrl+C (which runs
    # the 'except' block)
    try:
        target = now()
        one_second_later = datetime.timedelta(seconds=1)
        if platform.system() == 'Windows':
            os.system('cls')
            os.system('title ~~~ Shaking the Eightball ~~~')
            os.system('color 20') # Set background color to green, foreground to black
            os.system('mode con: cols=53 lines=22') # Set window to smaller size
        else:
            pass # Need to write Linux version
        # Create loop to control the placement of the 'eightball'
        timesthru = 0
        num_indents = 0
        for remaining in range(nap_length, 0, -1): # Countdown from nap_length to zero
            target += one_second_later
            os.system('cls')
            if timesthru < 5:
                # Move the ball right 5 times
                timesthru += 1
                num_indents += 1
            elif (timesthru >= 5) and (timesthru <= 8):
                # Move the ball left 5 times
                timesthru += 1
                num_indents -= 1
            else:
                # Start over
                timesthru = 0
                num_indents = 0
            # Show 'da_ball', indented 'num_indents' times
            print(indent(da_ball,num_indents))
            # Show how long til the next sound
            print(f'{"Sleeping for ":>25}{str(remaining)}{" seconds..."}')
            # Show how many unplayed files are left in the list
            print(f'\n{"Unique files left to play: ":>37}{len(all_filenames)}')
            # If there are still seconds left, sleep 1 second before restarting the loop
            if (target - now()).total_seconds() >= 0:
                time.sleep((target - now()).total_seconds())
        # Now that the loop has ended, play the next sound
        get_it()

    except KeyboardInterrupt: # KeyboardInterrupt = Ctrl+C
        os.system('cls')
        os.system('color 07')
        os.system('mode con: cols=120 lines=30')
        exit()


def indent(a_string, num_indents=1):
    # Indent 'da_ball' 'num_indents' times and give it back
    times = 0
    while times < num_indents:
        a_string = a_string.replace('\n', '\n     ')
        times += 1
    return a_string


if __name__ == '__main__':
    all_filenames = []
    da_ball = """

        _.a$$$$$a._
      ,$$$$$$$$$$$$$.
    ,$$$$$$$$$$$$$$$$$.
   d$$$$$$$$$$$$$$$$$$$b
  d$$$$$$$$~'"`~$$$$$$$$b
 ($$$$$$$p   _   q$$$$$$$)
 $$$$$$$$   (_)   $$$$$$$$
 $$$$$$$$   (_)   $$$$$$$$
 ($$$$$$$b       d$$$$$$$)
  q$$$$$$$$a._.a$$$$$$$$p
   q$$$$$$$$$$$$$$$$$$$p
    `$$$$$$$$$$$$$$$$$'
      `$$$$$$$$$$$$$'
        `~$$$$$$$~'
            ''' """
    get_it()
    os.system('cls')
    os.system('color 07')
    os.system('mode con: cols=120 lines=30')
