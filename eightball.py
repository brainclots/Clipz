#!/usr/local/bin/python3
import glob
import random
import os
import datetime
import time
import sys

def get_it():
    google_drive = os.getenv('GDRIVE')
    google_drive = google_drive.replace('"', '')
    target_dir = os.path.normpath(google_drive + '/Music/Soundz/Clipz')
    wav_filenames = glob.glob(target_dir + '/*.wav')
    mp3_filenames = glob.glob(target_dir + '/*.mp3')

    all_filenames = wav_filenames + mp3_filenames
    all_filenames.sort(key=str.lower)
    lucky_one = random.choice(all_filenames)
    word_file = lucky_one + ".txt"

    if os.path.isfile(word_file):
        clip_file = open(word_file, 'r')
    else:
        clip_file_path = target_dir + '/snarky.txt'
        clip_file = open(clip_file_path, 'r')

    clip_txt = clip_file.read()
    num_lines = clip_txt.count('\n')
    clip_file.close()

    window_height = 29 + num_lines
    # Set window size to the right height in lines and 120 characters wide
    #os.system('printf \033[8\;%d\;120t' % window_height)
    #os.system('tput clear')
    os.system(f'mode con: cols=120 lines={window_height}')
    os.system('color 3f')
    # Show the top of the bubble
    print(" __________________  ")
    print("/                  \ ")
    # Show the contents of the words text file
    print(clip_txt, end="")
    shark = open(target_dir + '/snarkshark_short.txt', 'r')
    shark_txt = shark.read()
    shark.close()
    print(shark_txt, end=" ")
    lucky_parens = '( ' + os.path.basename(lucky_one) + ' )'
    print(f'{" ":75}{lucky_parens:^20}')

    os.system(f'title Playing {os.path.basename(lucky_one)}')
    os.system(f'swavplayer "{lucky_one}"')
    #os.system(f'afplay -v .2 {lucky_one})
    #os.system('printf \033[8\;30\;120t')
    #os.system('ttytle')
    #os.system('tput clear')
    track_it(all_filenames, lucky_one)


def track_it(all_filenames, lucky_one):
    # Keep track for statistics
    totalcount = len(all_filenames)
    with open('eightball.log', 'a') as f:
        now = datetime.datetime.now().strftime('%m/%d/%Y,%H:%M:%S')
        f.write(f'{now},{all_filenames.index(lucky_one)},{totalcount},{os.path.basename(lucky_one)}\n')
    nap_length = random.randrange(15, 120)
    rest_it(nap_length)


def rest_it(nap_length, now=datetime.datetime.now):
    if len(sys.argv) > 1:
        try:
            target = now()
            one_second_later = datetime.timedelta(seconds=1)
            file = 0
            direction = 'right'
            os.system('cls')
            os.system('title ~~~ Shaking the Eightball ~~~')
            os.system('color 20')
            os.system('mode con: cols=55 lines=22')
            for remaining in range(nap_length, 0, -1):
                target += one_second_later
                os.system('cls')
                print()
                os.system(f'type eightball{file}.txt')
                print()
                print(f'{" ":15}{"Sleeping for "}{str(remaining)}{" seconds..."}')
                if direction == 'right':
                    if file <= 3:
                        file += 1
                    else:
                        direction = 'left'
                else:
                    if file > 0:
                        file -= 1
                    else:
                        direction = 'right'
                time.sleep((target - now()).total_seconds())
            get_it()
        except KeyboardInterrupt:
            os.system('cls')
            os.system('color 07')
            os.system('mode con: cols=120 lines=30')
            exit()

if __name__ == '__main__':
    get_it()
    os.system('cls')
    os.system('color 07')
    os.system('mode con: cols=120 lines=30')
