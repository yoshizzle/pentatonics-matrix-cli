# minmaj7.py — Eb key center

SCALE_DATA = {
    "ebminmaj7": [
        {"notes": ("Eb", "Gb", "Bb", "D")},
        {"scales": [

            {"scale": "bb major b6",
             "notes": ("Gb", "Bb", "C", "D", "F"),
             "tensions": ("b3", "5", "13", "7", "9"),
             "order": 10},

            {"scale": "d whole tone",
             "notes": ("D", "F#", "G#", "Bb", "C"),
             "tensions": ("7", "b3", "11", "5", "13"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Eb", "F", "G", "B", "C#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Eb", "F", "Ab", "Bb", "C"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Eb", "E", "G", "A", "C"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Eb", "Gb", "A", "C", "Db"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
