# min7b5.py — Bb key center

SCALE_DATA = {
    "bbmin7b5": [
        {"notes": ("Bb", "Db", "E", "Ab")},
        {"scales": [

            {"scale": "Eb minor 6",
             "notes": ("Eb", "Gb", "Ab", "Bb", "C"),
             "tensions": ("b3", "b5", "13", "b7", "r"),
             "order": 10},

            {"scale": "Bb minor 7b5",
             "notes": ("Bb", "Db", "Eb", "E", "Ab"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "F minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

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
