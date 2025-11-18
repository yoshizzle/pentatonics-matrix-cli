# min6.py

SCALE_DATA = {
    "c#min6": [
        {"notes": ("C#", "E", "G#", "A#")},
        {"scales": [

            {"scale": "c# minor 6",
             "notes": ("C#", "E", "F#", "G#", "A#"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 10},

            {"scale": "a# minor 7b5",
             "notes": ("A#", "C#", "D#", "E", "G#"),
             "tensions": ("13", "r", "9", "b3", "5"),
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
