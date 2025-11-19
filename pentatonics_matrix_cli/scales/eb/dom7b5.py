# dom7b5.py — Eb key center

SCALE_DATA = {
    "eb7b5": [
        {"notes": ("Eb", "G", "B", "Db")},
        {"scales": [

            {"scale": "C minor 6",
             "notes": ("C", "Eb", "F", "G", "A"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "Eb minor 7b5",
             "notes": ("Eb", "Gb", "Ab", "B", "Db"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "F minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Eb", "F", "G", "B", "C"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Eb", "F", "Ab", "Bb", "C"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Eb", "E", "G", "B", "C"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Eb", "Gb", "A", "B", "Db"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},

            {"scale": "lydian dominant pentatonic",
             "notes": ("Eb", "F", "G", "A", "Db"),
             "tensions": ("r", "9", "3", "#11", "b7"),
             "order": 140}
        ]}
    ]
}
