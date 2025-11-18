# minmaj7.py — G key center

SCALE_DATA = {
    "gminmaj7": [
        {"notes": ("G", "Bb", "D", "F#")},
        {"scales": [

            {"scale": "e major b6",
             "notes": ("Bb", "D", "E", "F#", "A"),
             "tensions": ("b3", "5", "13", "7", "9"),
             "order": 10},

            {"scale": "b whole tone",
             "notes": ("B", "E", "F#", "G#", "A"),
             "tensions": ("7", "b3", "11", "5", "13"),
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
