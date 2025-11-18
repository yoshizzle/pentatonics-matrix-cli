# min6.py — F key center

SCALE_DATA = {
    "fmin6": [
        {"notes": ("F", "Ab", "C", "D")},
        {"scales": [

            {"scale": "f minor 6",
             "notes": ("F", "Ab", "Bb", "C", "D"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 10},

            {"scale": "d minor 7b5",
             "notes": ("D", "F", "G", "Ab", "C"),
             "tensions": ("13", "r", "9", "b3", "5"),
             "order": 20},

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
