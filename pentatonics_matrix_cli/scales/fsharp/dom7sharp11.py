# dom7sharp11.py — F# key center

SCALE_DATA = {
    "f#7#11": [
        {"notes": ("F#", "A#", "C#", "E", "B#")},
        {"scales": [

            {"scale": "c# whole tone",
             "notes": ("C#", "D#", "E#", "Fx", "G#"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "g# major b6",
             "notes": ("E", "G#", "A#", "B#", "D#"),
             "tensions": ("b7", "9", "3", "#11", "5"),
             "order": 20},

            {"scale": "d# minor 6",
             "notes": ("D#", "F#", "G#", "A#", "B#"),
             "tensions": ("13", "r", "9", "3", "#11"),
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
