# min6.py — B key center

SCALE_DATA = {
    "bmin6": [
        {"notes": ("B", "D", "F#", "G#")},
        {"scales": [

            {"scale": "B minor 6",
             "notes": ("B", "D", "E", "F#", "G#"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 10},

            {"scale": "G# minor 7b5",
             "notes": ("G#", "B", "C#", "D", "F#"),
             "tensions": ("13", "r", "9", "b3", "5"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("B", "C#", "D#", "G", "A"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("B", "C#", "E", "F#", "G#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("B", "C", "D#", "G", "A"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("B", "D", "F", "F#", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
