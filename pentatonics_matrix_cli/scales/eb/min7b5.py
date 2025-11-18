# min7b5.py — Eb key center

SCALE_DATA = {
    "ebmin7b5": [
        {"notes": ("Eb", "Gb", "A", "Db")},
        {"scales": [

            {"scale": "gb minor 6",
             "notes": ("Gb", "A", "B", "Db", "Eb"),
             "tensions": ("b3", "b5", "13", "b7", "r"),
             "order": 10},

            {"scale": "eb minor 7b5",
             "notes": ("Eb", "Gb", "A", "Bb", "Db"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "ab minor",
             "notes": ("Ab", "B", "Db", "Eb", "Gb"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

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
