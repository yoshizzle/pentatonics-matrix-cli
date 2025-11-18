# minmaj7.py

SCALE_DATA = {
    "cminmaj7": [
        {"notes": ("C", "Eb", "G", "B")},
        {"scales": [
            {"scale": "g major b6", "notes": ("Eb", "G", "A", "B", "D"),
             "tensions": ("b3", "5", "13", "7", "9"), "order": 10},

            {"scale": "b whole tone", "notes": ("B", "Eb", "F", "G", "A"),
             "tensions": ("7", "b3", "11", "5", "13"), "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "Eb", "G#", "A#"),
             "tensions": ("r", "9", "b3", "#5", "7"),
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
             "tensions": ("r", "b3", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
