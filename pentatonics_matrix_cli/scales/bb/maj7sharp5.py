# maj7sharp5.py — Bb key center

SCALE_DATA = {
    "bbmaj7#5": [
        {"notes": ("Bb", "D", "F#", "A")},
        {"scales": [

            {"scale": "F major b6",
             "notes": ("Bb", "D", "G", "F#", "A"),
             "tensions": ("r", "3", "#11", "#5", "7"),
             "order": 10},

            {"scale": "C minor 6",
             "notes": ("C", "Eb", "F", "G", "A"),
             "tensions": ("7", "9", "3", "#11", "#5"),
             "order": 20},

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
