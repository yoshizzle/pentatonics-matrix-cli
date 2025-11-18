# min6.py — Ab key center

SCALE_DATA = {
    "abmin6": [
        {"notes": ("Ab", "Cb", "Eb", "F")},
        {"scales": [

            {"scale": "Ab minor 6",
             "notes": ("Ab", "Cb", "Db", "Eb", "F"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 10},

            {"scale": "F minor 7b5",
             "notes": ("F", "Ab", "Bb", "Cb", "Eb"),
             "tensions": ("13", "r", "9", "b3", "5"),
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
