#! python3

# This script takes a sentence as input and produces a text file with that
# sentence centered and surrounded by pipe symbols '|' for use with the
# snark shark randomizer known as 'eightball.py'.

import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('soundfile', nargs=1)
parser.add_argument('words', nargs='*')
args = parser.parse_args()


def storeInDict(linedict, linenum, pline):
    "Function to write a line of potential words to the linedict dictionary"
    linenum += 1
    linedict[linenum] = pline
    pline = []
    linelen = 0
    return linedict[linenum], linenum, linelen, pline


def main():
    soundfile = args.soundfile[0]
    words = args.words

    if not os.path.isfile(soundfile):
        print(f'The first argument must be the name of the sound file, and \"{soundfile}\" does not exist!')
        return
    edge = '|'
    linelen = 0
    linenum = 0
    currentword = 0
    desiredwidth = 19
    pline = []          # Potential line list
    linedict = {}       # Line dictionary in {1: [first, line], 2: [second, line]} format.

# See if multiple words fit on one line
    while (currentword < len(words)): # While we still have words left:
        if (words[currentword] == "\\n"): # If the current word is '\n', don't append, just write that line to the dictionary and move on.
            linedict[linenum], linenum, linelen, pline = storeInDict(linedict, linenum, pline)
            currentword += 1
        else:
            linelen += len(words[currentword]) + 1 # Add the length of that word, plus one for a space, to the line length.
            if linelen < desiredwidth: # If line length is less than desired width:
                pline.append(words[currentword]) # Append the word to the potential line list of words and move on.
                currentword += 1
            else: # Once we hit or exceed the desired length, write the potential line list to the dictionary.
                linedict[linenum], linenum, linelen, pline = storeInDict(linedict, linenum, pline)
    else: # Last words on the last line.
        linedict[linenum] = pline

# Print out the formatted lines
    outfile = open(f"{soundfile}.txt", "w")
    for eachline in sorted(linedict.keys()):
        line = ' '.join(linedict[eachline])
        line = line.strip('\\')
        outfile.write(f'{edge}{line.center(19)}{edge}\n')
    outfile.close()
    os.system(f"test_it.bat {soundfile}")

main()
