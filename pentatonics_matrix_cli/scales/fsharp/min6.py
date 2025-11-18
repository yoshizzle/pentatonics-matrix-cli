# min6.py — F# key center

SCALE_DATA = {
    "f#min6": [
        {"notes": ("F#", "A", "C#", "D#")},
        {"scales": [

            {"scale": "f# minor 6",
             "notes": ("F#", "A", "B", "C#", "D#"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 10},

            {"scale": "d# minor 7b5",
             "notes": ("D#", "F#", "G#", "A", "C#"),
             "tensions": ("13", "r", "9", "b3", "5"),
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
