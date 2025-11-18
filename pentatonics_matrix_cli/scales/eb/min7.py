# min7.py — Eb key center

SCALE_DATA = {
    "ebmin7": [
        {"notes": ("Eb", "Gb", "Bb", "Db")},
        {"scales": [

            {"scale": "eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 10},

            {"scale": "bb minor",
             "notes": ("Bb", "Db", "Eb", "F", "Ab"),
             "tensions": ("5", "b7", "r", "9", "11"),
             "order": 20},

            {"scale": "f minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 30},

            {"scale": "db minor",
             "notes": ("Db", "E", "Gb", "Ab", "B"),
             "tensions": ("b7", "b9", "b3", "11", "13"),
             "order": 40},

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
