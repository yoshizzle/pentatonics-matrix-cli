# dom7b5.py — D key center

SCALE_DATA = {
    "d7b5": [
        {"notes": ("D", "F#", "A#", "C")},
        {"scales": [

            {"scale": "A minor 6",
             "notes": ("A", "C", "D", "E", "F#"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "D minor 7b5",
             "notes": ("D", "F", "G", "A#", "C"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "G minor",
             "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("D", "E", "F#", "A#", "C#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("D", "E", "G", "A", "B"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("D", "Eb", "F#", "A#", "C#"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("D", "F", "Ab", "A#", "C"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},

            {"scale": "lydian dominant pentatonic",
             "notes": ("D", "E", "F#", "G#", "C"),
             "tensions": ("r", "9", "3", "#11", "b7"),
             "order": 140}
        ]}
    ]
}
