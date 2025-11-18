# maj7.py — Ab key center

SCALE_DATA = {
    "abmaj7": [
        {"notes": ("Ab", "C", "Eb", "G")},
        {"scales": [

            {"scale": "f minor",
             "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("13", "r", "3", "11", "5"),
             "order": 10},

            {"scale": "c minor",
             "notes": ("C", "Eb", "F", "G", "Bb"),
             "tensions": ("3", "5", "13", "7", "9"),
             "order": 20},

            {"scale": "a minor",
             "notes": ("A", "C", "D", "E", "G"),
             "tensions": ("7", "9", "3", "#11", "13"),
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
