import sys
import texttable

from scales import scales as matrix

root_set = ("C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab","A","Bb","B","Cb")
chord_type_set = ("Maj7","Maj7#11","Maj7#5","Maj7b5","min7","min6","7","7#11","7b9sus","7nat9b13","7alt","min7b5","min7b5nat9","min/Maj7")
scale_list = []
scale_list.append(["Pent Scale", "Notes", "Tensions"])



def main():
    print("Exit at any time by typing 'quit' and then [ENTER]\n")

    while True:
        root = input("Please enter a root note {}: ".format(root_set))
        if root == 'quit':
            sys.exit(0)
        elif root not in root_set:
            print("Invalid root note")
            continue
        else:
            break
            main()

    while True:
        chord_type = input("Please enter a chord type {}: ".format(chord_type_set))
        if chord_type == 'quit':
            sys.exit(0)
        elif chord_type not in chord_type_set:
            print("Invalid chord type")
            continue
        else:
            break
            main()

    chord = root + chord_type

    if chord in matrix:
        for x in range(1):
            print()

        print("You can play the following pentatonic scales over a {} chord: ".format(chord))
        print("The chord tones are: {}".format(matrix[chord][0]['notes']))

        for x in range(1):
            print()

        mtx = texttable.Texttable()
        mtx.set_cols_width([20,50,50])

        for scales in matrix[chord][1]:
            for scale in sorted(matrix[chord][1][scales], key=lambda k: k['order']):
                scale_list.append([scale['scale'], scale['notes'], scale['tensions']])

        mtx.add_rows(scale_list)
        print(mtx.draw())
    else:
        print("Chord not found")

    main()

if __name__ == "__main__":
    main()


