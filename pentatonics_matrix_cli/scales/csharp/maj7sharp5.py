# maj7sharp5.py

SCALE_DATA = {
    "c#maj7#5": [
        {"notes": ("C#", "E#", "Gx", "B#")},
        {"scales": [

            {"scale": "e# major b6",
             "notes": ("C#", "E#", "Fx", "Gx", "B#"),
             "tensions": ("r", "3", "#11", "#5", "7"),
             "order": 10},

            {"scale": "b# minor 6",
             "notes": ("B#", "D#", "E#", "Fx", "Gx"),
             "tensions": ("7", "9", "3", "#11", "#5"),
             "order": 20},

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
