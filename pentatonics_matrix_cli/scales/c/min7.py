# min7.py

SCALE_DATA = {
    "cmin7": [
        {"notes": ("C", "Eb", "G", "Bb")},
        {"scales": [
            {"scale": "c minor", "notes": ("C", "Eb", "F", "G", "Bb"),
             "tensions": ("r", "b3", "11", "5", "b7"), "order": 10},

            {"scale": "g minor", "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("5", "b7", "r", "9", "11"), "order": 20},

            {"scale": "d minor", "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("9", "11", "5", "13", "r"), "order": 30},

            {"scale": "bb minor", "notes": ("Bb", "Db", "Eb", "F", "Ab"),
             "tensions": ("b7", "b9", "b3", "11", "13"), "order": 40},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "Eb", "G", "A"),
             "tensions": ("r", "9", "b3", "5", "13"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C", "D", "F", "G", "Bb"),
             "tensions": ("r", "9", "11", "5", "b7"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C", "Db", "Eb", "Gb", "A"),
             "tensions": ("r", "b9", "b3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C", "Eb", "Gb", "A", "Bb"),
             "tensions": ("r", "b3", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
