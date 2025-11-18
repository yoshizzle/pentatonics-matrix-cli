# min7b5.py — F# key center

SCALE_DATA = {
    "f#min7b5": [
        {"notes": ("F#", "A", "C", "E")},
        {"scales": [

            {"scale": "A# minor 6",
             "notes": ("A#", "C#", "D#", "F#", "A"),
             "tensions": ("b3", "b5", "13", "b7", "r"),
             "order": 10},

            {"scale": "F# minor 7b5",
             "notes": ("F#", "A", "B", "C", "E"),
             "tensions": ("r", "b3", "11", "b5", "b7"),
             "order": 20},

            {"scale": "C# minor",
             "notes": ("C#", "E", "F#", "A", "B"),
             "tensions": ("11", "13", "b7", "r", "b3"),
             "order": 30},

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
