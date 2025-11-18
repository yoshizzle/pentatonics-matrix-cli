# minmaj7.py — F# key center

SCALE_DATA = {
    "f#minmaj7": [
        {"notes": ("F#", "A", "C#", "E#")},
        {"scales": [

            {"scale": "c# major b6",
             "notes": ("A", "C#", "D#", "E#", "G#"),
             "tensions": ("b3", "5", "13", "7", "9"),
             "order": 10},

            {"scale": "e# whole tone",
             "notes": ("E#", "Gx", "Ax", "B#", "D#"),
             "tensions": ("7", "b3", "11", "5", "13"),
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
