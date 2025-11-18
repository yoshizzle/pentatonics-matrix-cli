# maj7.py — G key center

SCALE_DATA = {
    "gmaj7": [
        {"notes": ("G", "B", "D", "F#")},
        {"scales": [

            {"scale": "e minor",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("13", "r", "3", "11", "5"),
             "order": 10},

            {"scale": "b minor",
             "notes": ("B", "D", "E", "F#", "A"),
             "tensions": ("3", "5", "13", "7", "9"),
             "order": 20},

            {"scale": "f# minor",
             "notes": ("F#", "A", "B", "C#", "E"),
             "tensions": ("7", "9", "3", "#11", "13"),
             "order": 30},

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
