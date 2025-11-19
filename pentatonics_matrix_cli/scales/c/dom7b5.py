# dom7b5.py — C key center

SCALE_DATA = {
    "c7b5": [
        {"notes": ("C", "E", "Gb", "Bb")},
        {"scales": [

            {"scale": "E minor 6",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "C minor 7b5",
             "notes": ("C", "Eb", "F", "Gb", "Bb"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "F minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "E", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C", "D", "F", "G", "A"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C", "Db", "E", "Gb", "A"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C", "Eb", "Gb", "A", "Bb"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},

            {"scale": "lydian dominant pentatonic",
             "notes": ("C", "D", "E", "F#", "Bb"),
             "tensions": ("r", "9", "3", "#11", "b7"),
             "order": 140}
        ]}
    ]
}
