# min7b5.py — F key center

SCALE_DATA = {
    "fmin7b5": [
        {"notes": ("F", "Ab", "B", "Eb")},
        {"scales": [

            {"scale": "ab minor 6",
             "notes": ("Ab", "B", "Db", "Eb", "F"),
             "tensions": ("b3", "b5", "13", "b7", "r"),
             "order": 10},

            {"scale": "f minor 7b5",
             "notes": ("F", "Ab", "Bb", "B", "Eb"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "bb minor",
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
