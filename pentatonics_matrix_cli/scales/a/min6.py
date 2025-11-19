# min6.py — A key center

SCALE_DATA = {
    "amin6": [
        {"notes": ("A", "C", "E", "F#")},
        {"scales": [

            {"scale": "A minor 6",
             "notes": ("A", "C", "D", "E", "F#"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 10},

            {"scale": "F# minor 7b5",
             "notes": ("F#", "A", "B", "C", "E"),
             "tensions": ("13", "r", "9", "b3", "5"),
             "order": 20},

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
