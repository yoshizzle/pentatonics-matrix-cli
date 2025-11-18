# maj7sharp5.py — G key center

SCALE_DATA = {
    "gmaj7#5": [
        {"notes": ("G", "B", "D#", "F#")},
        {"scales": [

            {"scale": "e major b6",
             "notes": ("G", "B", "C#", "D#", "F#"),
             "tensions": ("r", "3", "#11", "#5", "7"),
             "order": 10},

            {"scale": "b minor 6",
             "notes": ("B", "D", "E", "F#", "D#"),
             "tensions": ("7", "9", "3", "#11", "#5"),
             "order": 20},

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
