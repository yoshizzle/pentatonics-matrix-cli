# dom7b5.py — G key center

SCALE_DATA = {
    "g7b5": [
        {"notes": ("G", "B", "D#", "F")},
        {"scales": [

            {"scale": "E minor 6",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "G minor 7b5",
             "notes": ("G", "Bb", "C", "D#", "F"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "C minor",
             "notes": ("C", "Eb", "F", "G", "Bb"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("G", "A", "B", "D#", "F#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("G", "A", "C", "D", "E"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("G", "Ab", "B", "D#", "F#"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("G", "Bb", "Db", "D#", "F#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},

            {"scale": "lydian dominant pentatonic",
             "notes": ("G", "A", "B", "C#", "F"),
             "tensions": ("r", "9", "3", "#11", "b7"),
             "order": 140}
        ]}
    ]
}
