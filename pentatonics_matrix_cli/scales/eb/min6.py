# min6.py — Eb key center

SCALE_DATA = {
    "ebmin6": [
        {"notes": ("Eb", "Gb", "Bb", "C")},
        {"scales": [

            {"scale": "eb minor 6",
             "notes": ("Eb", "Gb", "Ab", "Bb", "C"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 10},

            {"scale": "c minor 7b5",
             "notes": ("C", "Eb", "F", "Gb", "Bb"),
             "tensions": ("13", "r", "9", "b3", "5"),
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
