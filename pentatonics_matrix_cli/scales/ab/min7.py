# min7.py — Ab key center

SCALE_DATA = {
    "abmin7": [
        {"notes": ("Ab", "Cb", "Eb", "Gb")},
        {"scales": [

            {"scale": "Ab minor",
             "notes": ("Ab", "Cb", "Db", "Eb", "Gb"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 10},

            {"scale": "Eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("5", "b7", "r", "9", "11"),
             "order": 20},

            {"scale": "Bb minor",
             "notes": ("Bb", "Db", "Eb", "F", "Ab"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 30},

            {"scale": "F minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("b7", "b9", "b3", "11", "13"),
             "order": 40},

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
