# maj7b5.py — A key center

SCALE_DATA = {
    "amaj7b5": [
        {"notes": ("A", "C#", "E", "G#")},
        {"scales": [

            {"scale": "E minor 7b5",
             "notes": ("E", "G", "A", "C", "D"),
             "tensions": ("b5", "13", "7", "r", "3"),
             "order": 10},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("A", "B", "C#", "F", "G"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("A", "B", "D", "E", "F#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("A", "Bb", "C#", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("A", "C", "Eb", "F#", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
