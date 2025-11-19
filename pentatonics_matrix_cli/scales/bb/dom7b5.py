# dom7b5.py — Bb key center

SCALE_DATA = {
    "bb7b5": [
        {"notes": ("Bb", "D", "F#", "Ab")},
        {"scales": [

            {"scale": "G minor 6",
             "notes": ("G", "Bb", "C", "D", "E"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "Bb minor 7b5",
             "notes": ("Bb", "Db", "Eb", "F#", "Ab"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "Eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Bb", "C", "D", "F#", "G"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Bb", "C", "Eb", "F", "G"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Bb", "B", "D", "F#", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Bb", "Db", "F", "F#", "G"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},

            {"scale": "lydian dominant pentatonic",
             "notes": ("Bb", "C", "D", "E", "G"),
             "tensions": ("r", "9", "3", "#11", "b7"),
             "order": 140}
        ]}
    ]
}
