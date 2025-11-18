# dom7sharp11.py — Ab key center

SCALE_DATA = {
    "ab7#11": [
        {"notes": ("Ab", "C", "Eb", "Gb", "D")},
        {"scales": [

            {"scale": "F whole tone",
             "notes": ("F", "Ab", "Bb", "C", "D"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "A major b6",
             "notes": ("F", "A", "Bb", "D", "Eb"),
             "tensions": ("b7", "9", "3", "#11", "5"),
             "order": 20},

            {"scale": "E minor 6",
             "notes": ("E", "G", "A", "Bb", "D"),
             "tensions": ("13", "r", "9", "3", "#11"),
             "order": 30},

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
