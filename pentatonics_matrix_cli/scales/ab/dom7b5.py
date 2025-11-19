# dom7b5.py — Ab key center

SCALE_DATA = {
    "ab7b5": [
        {"notes": ("Ab", "C", "E", "Gb")},
        {"scales": [

            {"scale": "F minor 6",
             "notes": ("F", "Ab", "Bb", "C", "D"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "Ab minor 7b5",
             "notes": ("Ab", "B", "Db", "E", "Gb"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "Db minor",
             "notes": ("Db", "E", "Gb", "Ab", "B"),
             "tensions": ("11", "13", "b7", "r", "b3"),
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
             "notes": ("Ab", "B", "D", "E", "Gb"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130},

            {"scale": "lydian dominant pentatonic",
             "notes": ("Ab", "Bb", "C", "D", "Gb"),
             "tensions": ("r", "9", "3", "#11", "b7"),
             "order": 140}
        ]}
    ]
}
