# minmaj7.py — Ab key center

SCALE_DATA = {
    "abminmaj7": [
        {"notes": ("Ab", "Cb", "Eb", "G")},
        {"scales": [

            {"scale": "Eb major b6",
             "notes": ("Cb", "Eb", "F", "G", "Bb"),
             "tensions": ("b3", "5", "13", "7", "9"),
             "order": 10},

            {"scale": "B whole tone",
             "notes": ("B", "Eb", "F", "G", "A"),
             "tensions": ("7", "b3", "11", "5", "13"),
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
