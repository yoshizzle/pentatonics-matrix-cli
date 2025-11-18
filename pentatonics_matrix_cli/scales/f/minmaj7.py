# minmaj7.py — F key center

SCALE_DATA = {
    "fminmaj7": [
        {"notes": ("F", "Ab", "C", "E")},
        {"scales": [

            {"scale": "c major b6",
             "notes": ("Ab", "C", "D", "E", "G"),
             "tensions": ("b3", "5", "13", "7", "9"),
             "order": 10},

            {"scale": "e whole tone",
             "notes": ("E", "G#", "A#", "C", "D"),
             "tensions": ("7", "b3", "11", "5", "13"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("F", "G", "A", "C#", "D#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("F", "G", "Bb", "C", "D"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("F", "Gb", "A", "B", "D"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("F", "Ab", "B", "D", "Eb"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
