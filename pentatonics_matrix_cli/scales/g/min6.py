# min6.py — G key center

SCALE_DATA = {
    "gmin6": [
        {"notes": ("G", "Bb", "D", "E")},
        {"scales": [

            {"scale": "g minor 6",
             "notes": ("G", "Bb", "C", "D", "E"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 10},

            {"scale": "e minor 7b5",
             "notes": ("E", "G", "A", "Bb", "D"),
             "tensions": ("13", "r", "9", "b3", "5"),
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
