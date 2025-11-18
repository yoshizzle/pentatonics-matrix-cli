# minmaj7.py

SCALE_DATA = {
    "c#minmaj7": [
        {"notes": ("C#", "E", "G#", "B#")},
        {"scales": [

            {"scale": "g# major b6",
             "notes": ("E", "G#", "A#", "B#", "D#"),
             "tensions": ("b3", "5", "13", "7", "9"),
             "order": 10},

            {"scale": "b# whole tone",
             "notes": ("B#", "E", "F#", "G#", "A#"),
             "tensions": ("7", "b3", "11", "5", "13"),
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
