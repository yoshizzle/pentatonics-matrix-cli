# dom7flat9sus.py — G key center

SCALE_DATA = {
    "g7b9sus": [
        {"notes": ("G", "C", "D", "F", "Ab")},
        {"scales": [

            {"scale": "C minor 6",
             "notes": ("C", "Eb", "F", "G", "A"),
             "tensions": ("b7", "b9", "#9", "11", "13"),
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
