# min7.py — F# key center

SCALE_DATA = {
    "f#min7": [
        {"notes": ("F#", "A", "C#", "E")},
        {"scales": [

            {"scale": "f# minor",
             "notes": ("F#", "A", "B", "C#", "E"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 10},

            {"scale": "c# minor",
             "notes": ("C#", "E", "F#", "G#", "B"),
             "tensions": ("5", "b7", "r", "9", "11"),
             "order": 20},

            {"scale": "g# minor",
             "notes": ("G#", "B", "C#", "D#", "F#"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 30},

            {"scale": "e# minor",
             "notes": ("E#", "G#", "A#", "B#", "D#"),
             "tensions": ("b7", "b9", "b3", "11", "13"),
             "order": 40},

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
