# maj7sharp5.py — F key center

SCALE_DATA = {
    "fmaj7#5": [
        {"notes": ("F", "A", "C#", "E")},
        {"scales": [

            {"scale": "a major b6",
             "notes": ("F", "A", "B", "C#", "E"),
             "tensions": ("r", "3", "#11", "#5", "7"),
             "order": 10},

            {"scale": "e minor 6",
             "notes": ("E", "G", "A", "B", "C#"),
             "tensions": ("7", "9", "3", "#11", "#5"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("F", "G", "A", "C#", "D#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("F", "G", "Bb", "C", "D"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("F", "Gb", "A", "B", "D"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("F", "Ab", "B", "D", "Eb"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
