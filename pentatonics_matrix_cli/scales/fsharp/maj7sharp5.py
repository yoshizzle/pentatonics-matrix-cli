# maj7sharp5.py — F# key center

SCALE_DATA = {
    "f#maj7#5": [
        {"notes": ("F#", "A#", "Cx", "E#")},
        {"scales": [

            {"scale": "a# major b6",
             "notes": ("F#", "A#", "B#", "Cx", "E#"),
             "tensions": ("r", "3", "#11", "#5", "7"),
             "order": 10},

            {"scale": "e# minor 6",
             "notes": ("E#", "G#", "A#", "B#", "Cx"),
             "tensions": ("7", "9", "3", "#11", "#5"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("F#", "G#", "A#", "D", "E"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("F#", "G#", "B", "C#", "D#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("F#", "G", "A#", "C", "E"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("F#", "A", "C", "E", "E#"),
             "tensions": ("r", "#9", "b5", "13", "7"),
             "order": 130}
        ]}
    ]
}
