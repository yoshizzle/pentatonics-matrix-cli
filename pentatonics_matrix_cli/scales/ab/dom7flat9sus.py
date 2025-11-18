# dom7flat9sus.py — Ab key center

SCALE_DATA = {
    "ab7b9sus": [
        {"notes": ("Ab", "Db", "Eb", "Gb", "B")},
        {"scales": [

            {"scale": "Bb minor 6",
             "notes": ("Bb", "Db", "Eb", "F", "Ab"),
             "tensions": ("b7", "b9", "#9", "11", "13"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Ab", "Bb", "C", "E", "F"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Ab", "Bb", "Db", "Eb", "F"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Ab", "A", "C", "E", "F"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Ab", "Bb", "C", "Eb", "F#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
