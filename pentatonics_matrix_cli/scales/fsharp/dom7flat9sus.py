# dom7flat9sus.py — F# key center

SCALE_DATA = {
    "f#7b9sus": [
        {"notes": ("F#", "B", "C#", "E", "G")},
        {"scales": [

            {"scale": "b minor 6",
             "notes": ("B", "D#", "E#", "F#", "A#"),
             "tensions": ("b7", "b9", "#9", "11", "13"),
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
