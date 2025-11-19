# maj7sharp5.py — B key center

SCALE_DATA = {
    "bmaj7#5": [
        {"notes": ("B", "D#", "G", "A#")},
        {"scales": [

            {"scale": "F# major b6",
             "notes": ("B", "D#", "E#", "G", "A#"),
             "tensions": ("r", "3", "#11", "#5", "7"),
             "order": 10},

            {"scale": "A# minor 6",
             "notes": ("A#", "C#", "D#", "E#", "G"),
             "tensions": ("7", "9", "3", "#11", "#5"),
             "order": 20},

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
             "order": 130}
        ]}
    ]
}
