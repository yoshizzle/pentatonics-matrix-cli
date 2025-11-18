# maj7sharp11.py — G key center

SCALE_DATA = {
    "gmaj7#11": [
        {"notes": ("G", "B", "D", "F#", "C#")},
        {"scales": [

            {"scale": "e minor 6",
             "notes": ("E", "G", "A", "B", "C#"),
             "tensions": ("13", "r", "9", "3", "#11"),
             "order": 10},

            {"scale": "b minor",
             "notes": ("B", "D", "E", "F#", "A"),
             "tensions": ("7", "9", "3", "#11", "13"),
             "order": 20},

            {"scale": "f# whole tone",
             "notes": ("F#", "A#", "B#", "D", "E"),
             "tensions": ("#11", "7", "r", "9", "3"),
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
