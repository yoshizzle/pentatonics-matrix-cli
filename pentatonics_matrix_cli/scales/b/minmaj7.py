# minmaj7.py — B key center

SCALE_DATA = {
    "bminmaj7": [
        {"notes": ("B", "D", "F#", "A#")},
        {"scales": [

            {"scale": "G# major b6",
             "notes": ("D", "F#", "G#", "A#", "C#"),
             "tensions": ("b3", "5", "13", "7", "9"),
             "order": 10},

            {"scale": "A# whole tone",
             "notes": ("A#", "C#", "D#", "E#", "F##"),
             "tensions": ("7", "b3", "11", "5", "13"),
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
