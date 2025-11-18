# dom7sharp11.py — G key center

SCALE_DATA = {
    "g7#11": [
        {"notes": ("G", "B", "D", "F", "C#")},
        {"scales": [

            {"scale": "D whole tone",
             "notes": ("D", "F", "G", "A", "B"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "A major b6",
             "notes": ("F", "A", "B", "C#", "D"),
             "tensions": ("b7", "9", "3", "#11", "5"),
             "order": 20},

            {"scale": "E minor 6",
             "notes": ("E", "G", "A", "B", "C#"),
             "tensions": ("13", "r", "9", "3", "#11"),
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
