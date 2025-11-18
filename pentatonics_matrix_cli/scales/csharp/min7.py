# min7.py

SCALE_DATA = {
    "c#min7": [
        {"notes": ("C#", "E", "G#", "B")},
        {"scales": [

            {"scale": "c# minor",
             "notes": ("C#", "E", "F#", "G#", "B"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 10},

            {"scale": "g# minor",
             "notes": ("G#", "B", "C#", "D#", "F#"),
             "tensions": ("5", "b7", "r", "9", "11"),
             "order": 20},

            {"scale": "d# minor",
             "notes": ("D#", "F#", "G#", "A#", "C#"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 30},

            {"scale": "b minor",
             "notes": ("B", "D", "E", "F#", "A"),
             "tensions": ("b7", "b9", "3", "11", "13"),
             "order": 40},

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
