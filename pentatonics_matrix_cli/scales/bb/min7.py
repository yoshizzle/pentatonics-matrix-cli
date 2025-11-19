# min7.py — Bb key center

SCALE_DATA = {
    "bbmin7": [
        {"notes": ("Bb", "Db", "F", "Ab")},
        {"scales": [

            {"scale": "Bb minor",
             "notes": ("Bb", "Db", "Eb", "F", "Ab"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 10},

            {"scale": "F minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("5", "b7", "r", "9", "11"),
             "order": 20},

            {"scale": "C minor",
             "notes": ("C", "Eb", "F", "G", "Bb"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 30},

            {"scale": "G minor",
             "notes": ("G", "Bb", "C", "Db", "F"),
             "tensions": ("b7", "b9", "b3", "11", "13"),
             "order": 40},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Bb", "C", "D", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Bb", "C", "Eb", "F", "G"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Bb", "B", "D", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Bb", "C#", "E", "F", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
