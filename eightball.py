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
    google_drive = Path(os.environ['GDRIVE'])
    target_dir = google_drive / 'Music/Soundz/Clipz'
    listofiles = target_dir / 'listofiles.tmp'
    if listofiles.is_file():
        all_filenames = listofiles.read_text().splitlines()
    if len(all_filenames) == 0:
        wav_filenames = list(target_dir.glob('*.wav'))
        mp3_filenames = list(target_dir.glob('*.mp3'))
        all_filenames = wav_filenames + mp3_filenames
    # Pick the 'lucky_one' and shuffle the list
    random.shuffle(all_filenames)
    lucky_one = all_filenames.pop()
    if str(lucky_one).startswith('%GDRIVE%'):
        lucky_one = lucky_one.replace('%GDRIVE%', str(google_drive))
    word_file = Path(str(lucky_one) + ".txt")
    # Get the words from the word_file
    if word_file.exists():
        clip_txt = word_file.read_text()
    else:
        clip_file_path = target_dir / 'snarky.txt'
        clip_txt = clip_file_path.read_text()
    num_lines = clip_txt.count('\n')
    # Write newly shuffled list of files back to list (without the 'lucky_one')
    with open(listofiles, 'w') as f:
        for item in all_filenames:
            if item:
                variabled_item = str(item).replace(r'C:\Users\bklotz\Google Drive','%GDRIVE%')
                f.write(f'{variabled_item}\n')

    # The height of the window should be the number of lines from the image
    # (img_lines) plus however many lines were in the word_file (num_lines)
    images = list(target_dir.glob('*_img.txt'))
    img = target_dir / random.choice(images)
    img_txt = img.read_text()
    img_lines = img_txt.count('\n')
    # Determine max width of the image
    width = 0
    for line in img_txt.splitlines():
        i = len(line)
        if i > width:
            width = i
    window_height = 5 + img_lines + num_lines
    # Set window size to the right height and width
    if OS == 'Windows':
        os.system(f'mode con: cols={width + 5} lines={window_height}') # Windows
        os.system('color F0') # Windows
    else:
        os.system(f'printf \033[8\;{window_height}\;{width}t') # Mac/Linux
        os.system('tput clear') # Mac/Linux
    # Show the top of the speech bubble
    print(" __________________  ")
    print("/                  \ ")
    # Show the contents of the words text file
    print(clip_txt, end="")
    #Show the rest of the image
    print(img_txt, end=" ")
    # Show the name of the file being played
    lucky_parens = '( ' + os.path.basename(lucky_one) + ' )'
    print(f'\n{lucky_parens:^{width}}')
    if os.path.exists(lucky_one):
        # Set the title and play the sound
        if OS == 'Windows':
            os.system(f'title Playing {os.path.basename(lucky_one)}') # Windows
            os.system(f'swavplayer "{lucky_one}"') # Windows
        else: # Mac/Linux
            os.system(f'afplay -v .2 {lucky_one}')
            os.system('printf \033[8\;30\;120t')
            os.system('ttytle')
            os.system('tput clear')
    else:
        print(f'Unable to locate {lucky_one}!')
        exit()
    # Run the function to log what was played and when
    track_it(all_filenames, lucky_one, img)


def track_it(all_filenames, lucky_one, img):
    # Keep track for statistics
    with open('eightball.log', 'a') as f:
        # Get the date and time in proper format
        now = datetime.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')
        # Add the line to the log
        f.write(f'{now},{os.path.basename(lucky_one)},{img.name}\n')
    # If running in a loop, pick a number between 15 and 120 seconds to wait
    if len(sys.argv) > 1:
        nap_length = random.randrange(15, 120)
        rest_it(nap_length)


def rest_it(nap_length, now=datetime.datetime.now):
    # 'try' block is to allow for a clean exit if pressing Ctrl+C (which runs
    # the 'except' block)
    try:
        if OS == 'Windows':
            clearcommand = 'cls'
        else:
            clearcommand = 'clear'
        target = now()
        one_second_later = datetime.timedelta(seconds=1)
        os.system(clearcommand)
        if OS == 'Windows':
            os.system('title ~~~ Shaking the Eightball ~~~')
            os.system('color 20') # Set background color to green, foreground to black
            os.system('mode con: cols=52 lines=22') # Set window to smaller size
        else:
            pass # Need to write Linux version
        # Create loop to control the placement of the 'eightball'
        timesthru = 0
        num_indents = 0
        for remaining in range(nap_length, 0, -1): # Countdown from nap_length to zero
            target += one_second_later
            os.system(clearcommand)
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
            print(f'{"Sleeping for ":>26}{str(remaining)}{" seconds..."}')
            # Show how many unplayed files are left in the list
            print(f'\n{"Unique files left to play: ":>37}{len(all_filenames)}')
            # If there are still seconds left, sleep 1 second before restarting the loop
            if (target - now()).total_seconds() >= 0:
                time.sleep((target - now()).total_seconds())
        # Now that the loop has ended, play the next sound
        get_it()

    except KeyboardInterrupt: # KeyboardInterrupt = Ctrl+C
        if OS == 'Windows':
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
    OS = platform.system()
    get_it()
    if OS == 'Windows':
        os.system('cls')
        os.system('color 07')
        os.system('mode con: cols=120 lines=30')
