# min7.py — G key center

SCALE_DATA = {
    "gmin7": [
        {"notes": ("G", "Bb", "D", "F")},
        {"scales": [

            {"scale": "g minor",
             "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 10},

            {"scale": "d minor",
             "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("5", "b7", "r", "9", "11"),
             "order": 20},

            {"scale": "a minor",
             "notes": ("A", "C", "D", "E", "G"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 30},

            {"scale": "e minor",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("b7", "b9", "b3", "11", "13"),
             "order": 40},

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
