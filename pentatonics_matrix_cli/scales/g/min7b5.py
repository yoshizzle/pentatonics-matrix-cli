# min7b5.py — G key center

SCALE_DATA = {
    "gmin7b5": [
        {"notes": ("G", "Bb", "Db", "F")},
        {"scales": [

            {"scale": "Bb minor 6",
             "notes": ("Bb", "Db", "Eb", "F", "G"),
             "tensions": ("b3", "b5", "13", "b7", "r"),
             "order": 10},

            {"scale": "G minor 7b5",
             "notes": ("G", "Bb", "C", "Db", "F"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "D minor",
             "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("G", "A", "B", "D#", "F"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("G", "A", "C", "D", "E"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("G", "Ab", "B", "D#", "F"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("G", "Bb", "D#", "F", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
