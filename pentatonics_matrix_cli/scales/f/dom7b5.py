# dom7b5.py — F key center

SCALE_DATA = {
    "f7b5": [
        {"notes": ("F", "A", "C#", "Eb")},
        {"scales": [

            {"scale": "D minor 6",
             "notes": ("D", "F", "G", "A", "B"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "F minor 7b5",
             "notes": ("F", "Ab", "Bb", "C#", "Eb"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "Bb minor",
             "notes": ("Bb", "Db", "Eb", "F", "Ab"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

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
             "notes": ("F", "Gb", "A", "C#", "D#"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("F", "Ab", "B", "C#", "Eb"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},

            {"scale": "lydian dominant pentatonic",
             "notes": ("F", "G", "A", "B", "Eb"),
             "tensions": ("r", "9", "3", "#11", "b7"),
             "order": 140}
        ]}
    ]
}
