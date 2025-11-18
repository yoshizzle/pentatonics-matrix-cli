# dom7nat9flat13.py

SCALE_DATA = {
    "c#7nat9b13": [
        {"notes": ("C#", "E#", "G#", "B", "D#", "A")},
        {"scales": [

            {"scale": "e# whole tone",
             "notes": ("E#", "Gx", "Ax", "Bx", "D#"),
             "tensions": ("3", "b13", "b7", "r", "9"),
             "order": 10},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C#", "D#", "E#", "Gx", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C#", "D#", "F#", "G#", "A#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C#", "D", "E#", "G", "A#"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C#", "E", "G", "A#", "B"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
