# maj7.py

SCALE_DATA = {
    "cmaj7": [
        {"notes": ("C", "E", "G", "B")},
        {"scales": [
            {"scale": "a minor", "notes": ("A", "C", "E", "F", "G"),
             "tensions": ("13", "r", "3", "11", "5"), "order": 10},

            {"scale": "e minor", "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("3", "5", "13", "7", "9"), "order": 20},

            {"scale": "b minor", "notes": ("B", "D", "E", "F#", "A"),
             "tensions": ("7", "9", "3", "#11", "13"), "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic", "notes": ("C", "D", "E", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"), "order": 100},

            {"scale": "mccoy pentatonic", "notes": ("C", "D", "F", "G", "A"),
             "tensions": ("r", "9", "11", "5", "13"), "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C", "Db", "E", "Gb", "A"),
             "tensions": ("r", "b9", "3", "b5", "13"), "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C", "Eb", "Gb", "A", "Bb"),
             "tensions": ("r", "#9", "b5", "13", "b7"), "order": 130}
        ]}
    ]
}
