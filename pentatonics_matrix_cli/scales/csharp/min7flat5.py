# min7flat5.py

SCALE_DATA = {
    "c#min7b5": [
        {"notes": ("C#", "E", "G", "B")},
        {"scales": [

            {"scale": "f# minor",
             "notes": ("F#", "A", "B", "C#", "E"),
             "tensions": ("11", "13", "b7", "r", "3"),
             "order": 10},

            {"scale": "e minor 6",
             "notes": ("E", "G", "A", "B", "C#"),
             "tensions": ("3", "b5", "13", "b7", "r"),
             "order": 20},

            {"scale": "c# minor 7b5",
             "notes": ("C#", "E", "F#", "G", "B"),
             "tensions": ("r", "b3", "11", "5", "b7"),
             "order": 30},

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
