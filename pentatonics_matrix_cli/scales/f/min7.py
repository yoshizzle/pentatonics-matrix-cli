# min7.py — F key center

SCALE_DATA = {
    "fmin7": [
        {"notes": ("F", "Ab", "C", "Eb")},
        {"scales": [

            {"scale": "f minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 10},

            {"scale": "c minor",
             "notes": ("C", "Eb", "F", "G", "Bb"),
             "tensions": ("5", "b7", "r", "9", "11"),
             "order": 20},

            {"scale": "g minor",
             "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 30},

            {"scale": "eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("b7", "b9", "b3", "11", "13"),
             "order": 40},

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
