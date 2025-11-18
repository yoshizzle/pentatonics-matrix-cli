# dom7nat9flat13.py — Ab key center

SCALE_DATA = {
    "ab7nat9b13": [
        {"notes": ("Ab", "C", "Eb", "Gb", "Bb", "F")},
        {"scales": [

            {"scale": "E whole tone",
             "notes": ("E", "G#", "A#", "B", "D"),
             "tensions": ("3", "b13", "b7", "r", "9"),
             "order": 10},

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
