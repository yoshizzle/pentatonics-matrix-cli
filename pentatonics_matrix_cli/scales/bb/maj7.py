# maj7.py — Bb key center

SCALE_DATA = {
    "bbmaj7": [
        {"notes": ("Bb", "D", "F", "A")},
        {"scales": [

            {"scale": "G minor",
             "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("13", "r", "3", "11", "5"),
             "order": 10},

            {"scale": "D minor",
             "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("3", "5", "13", "7", "9"),
             "order": 20},

            {"scale": "A minor",
             "notes": ("A", "C", "D", "E", "G"),
             "tensions": ("7", "9", "3", "#11", "13"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Bb", "C", "D", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Bb", "C", "Eb", "F", "G"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Bb", "B", "D", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Bb", "C#", "E", "F", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
