# min7.py — A key center

SCALE_DATA = {
    "amin7": [
        {"notes": ("A", "C", "E", "G")},
        {"scales": [

            {"scale": "A minor",
             "notes": ("A", "C", "D", "E", "G"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 10},

            {"scale": "E minor",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("5", "b7", "r", "9", "11"),
             "order": 20},

            {"scale": "B minor",
             "notes": ("B", "D", "E", "F#", "A"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 30},

            {"scale": "F# minor",
             "notes": ("F#", "A", "B", "C#", "E"),
             "tensions": ("b7", "b9", "b3", "11", "13"),
             "order": 40},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("A", "B", "C#", "F", "G"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("A", "B", "D", "E", "F#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("A", "Bb", "C#", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("A", "C", "Eb", "F#", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
