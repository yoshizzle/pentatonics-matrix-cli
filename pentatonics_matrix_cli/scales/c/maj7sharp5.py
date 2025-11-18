# maj7sharp5.py

SCALE_DATA = {
    "cmaj7#5": [
        {"notes": ("C", "E", "G#", "B")},
        {"scales": [
            {"scale": "e major b6", "notes": ("C", "E", "F#", "G#", "B"),
             "tensions": ("r", "3", "#11", "#5", "7"), "order": 10},

            {"scale": "b minor 6", "notes": ("B", "D", "E", "F#", "G#"),
             "tensions": ("7", "9", "3", "#11", "#5"), "order": 20},

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
