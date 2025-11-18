# dom7.py — F key center

SCALE_DATA = {
    "f7": [
        {"notes": ("F", "A", "C", "Eb")},
        {"scales": [

            {"scale": "c minor 6",
             "notes": ("C", "Eb", "F", "G", "A"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "g minor",
             "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 20},

            {"scale": "d minor",
             "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("13", "r", "9", "3", "5"),
             "order": 30},

            {"scale": "a minor 7b5",
             "notes": ("A", "C", "D", "Eb", "G"),
             "tensions": ("3", "5", "13", "b7", "9"),
             "order": 40},

            {"scale": "ab minor",
             "notes": ("Ab", "B", "Db", "Eb", "Gb"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 50},

            {"scale": "f major b2",
             "notes": ("F", "Gb", "A", "C", "D"),
             "tensions": ("r", "b9", "3", "5", "13"),
             "order": 60},

            {"scale": "ab major b2",
             "notes": ("Ab", "A", "C", "Eb", "F"),
             "tensions": ("#9", "3", "5", "b7", "r"),
             "order": 70},

            {"scale": "b major b2",
             "notes": ("B", "C", "D#", "F#", "G#"),
             "tensions": ("#11", "5", "b7", "b9", "#9"),
             "order": 80},

            {"scale": "d major b2",
             "notes": ("D", "Eb", "F#", "A", "B"),
             "tensions": ("13", "b7", "b9", "3", "#11"),
             "order": 90},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("F", "G", "A", "C#", "D#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("F", "G", "Bb", "C", "D"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("F", "Gb", "A", "B", "D"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("F", "Ab", "B", "D", "Eb"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
