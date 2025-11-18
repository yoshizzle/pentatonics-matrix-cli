# dom7sharp11.py — F key center

SCALE_DATA = {
    "f7#11": [
        {"notes": ("F", "A", "C", "Eb", "B")},
        {"scales": [

            {"scale": "c whole tone",
             "notes": ("C", "D", "E", "F#", "G#"),
             "tensions": ("5", "13", "3", "#11", "#5"),
             "order": 10},

            {"scale": "g major b6",
             "notes": ("Eb", "G", "A", "B", "D"),
             "tensions": ("b7", "9", "3", "#11", "13"),
             "order": 20},

            {"scale": "d minor 6",
             "notes": ("D", "F", "G", "A", "B"),
             "tensions": ("13", "r", "9", "3", "#11"),
             "order": 30},

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
