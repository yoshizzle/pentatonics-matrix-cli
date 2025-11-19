# dom7sharp11.py — Bb key center

SCALE_DATA = {
    "bb7#11": [
        {"notes": ("Bb", "D", "F", "Ab", "E")},
        {"scales": [

            {"scale": "G whole tone",
             "notes": ("G", "Bb", "C", "D", "E"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "D major b6",
             "notes": ("Bb", "D", "E", "F#", "G"),
             "tensions": ("b7", "9", "3", "#11", "5"),
             "order": 20},

            {"scale": "A minor 6",
             "notes": ("A", "C", "D", "E", "F#"),
             "tensions": ("13", "r", "9", "3", "#11"),
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
