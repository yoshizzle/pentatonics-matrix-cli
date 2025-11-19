# min7b5.py — A key center

SCALE_DATA = {
    "amin7b5": [
        {"notes": ("A", "C", "Eb", "G")},
        {"scales": [

            {"scale": "E minor 6",
             "notes": ("E", "G", "A", "B", "C"),
             "tensions": ("b3", "b5", "13", "b7", "r"),
             "order": 10},

            {"scale": "A minor 7b5",
             "notes": ("A", "C", "D", "Eb", "G"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "D minor",
             "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("A", "B", "C#", "F", "G"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("A", "B", "D", "E", "F#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("A", "Bb", "C#", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("A", "C", "Eb", "F#", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
