# maj7sharp5.py — Eb key center

SCALE_DATA = {
    "ebmaj7#5": [
        {"notes": ("Eb", "G", "B", "D")},
        {"scales": [

            {"scale": "g major b6",
             "notes": ("Eb", "G", "A", "B", "D"),
             "tensions": ("r", "3", "#11", "#5", "7"),
             "order": 10},

            {"scale": "d minor 6",
             "notes": ("D", "F", "G", "A", "B"),
             "tensions": ("7", "9", "3", "#11", "#5"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Eb", "F", "G", "B", "C#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Eb", "F", "Ab", "Bb", "C"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Eb", "E", "G", "A", "C"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Eb", "Gb", "A", "C", "Db"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
