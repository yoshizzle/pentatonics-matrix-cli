# dom7b5.py — B key center

SCALE_DATA = {
    "b7b5": [
        {"notes": ("B", "D#", "G", "A")},
        {"scales": [

            {"scale": "G# minor 6",
             "notes": ("G#", "B", "C#", "D#", "F#"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "B minor 7b5",
             "notes": ("B", "D", "E", "G", "A"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "E minor",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("B", "C#", "D#", "G", "A"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("B", "C#", "E", "F#", "G#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("B", "C", "D#", "G", "A"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("B", "D", "F", "F#", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},

            {"scale": "lydian dominant pentatonic",
             "notes": ("B", "C#", "D#", "F", "A"),
             "tensions": ("r", "9", "3", "#11", "b7"),
             "order": 140}
        ]}
    ]
}
