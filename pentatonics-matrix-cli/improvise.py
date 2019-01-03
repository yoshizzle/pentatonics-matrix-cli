import re
import sys
import texttable

from scales import scales as scales_matrix

ROOT_SET = ("C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab","A","Bb","B","Cb")
CHORD_TYPE_SET = ("Maj7","Maj7#11","Maj7#5","Maj7b5","min7","min6","7","7#11","7b9sus","7nat9b13","7alt","min7b5","min7b5nat9","min/Maj7")
MATRIX = [root+chord for root in ROOT_SET for chord in CHORD_TYPE_SET]
NOTE = re.compile('[a-gA-G][#bB]*')


def header():
    head = ("Welcome to the Pentatonics Matrix CLI. Please input your chord "
            "based on the following root notes and chord types:\n\nRoot Notes: "
            "{roots}\nChord Types: {chords}\n\nExample: CMaj7#11\n\n"
            "(Exit at any time by by typing 'quit' and then [ENTER].)\n\n".format(roots=ROOT_SET, chords=CHORD_TYPE_SET))


    return head

def main(show_header=False):
    scale_list = []
    scale_list.append(["Pentatonic Scale", "Notes", "Tensions"])

    if show_header:
        print(header())

    chord = input('\nChord: ')

    if chord == 'quit':
        sys.exit(0)
    elif chord not in MATRIX:
        print("Sorry, that chord does not exist. Please try again.\n")

        main()
    else:
        res = re.search(NOTE, chord)
        chord = NOTE.match(chord).group() + chord.split(res.group())[1]

        if chord in scales_matrix:
            print("\nThe chord tones for {} are: {}".format(chord, scales_matrix[chord][0]['notes']))
            print("\nYou can play the following pentatonic scales over a {} chord: ".format(chord))

            mtx = texttable.Texttable()
            mtx.set_cols_width([20,50,50])

            for pents in scales_matrix[chord][1]:
                for pent in sorted(scales_matrix[chord][1][pents], key=lambda k: k['order']):
                    scale_list.append([pent['scale'], pent['notes'], pent['tensions']])

            mtx.add_rows(scale_list)
            print(mtx.draw())

    main()


if __name__ == "__main__":
    main(show_header=True)

