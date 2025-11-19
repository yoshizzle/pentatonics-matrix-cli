# maj7.py — A key center

SCALE_DATA = {
    "amaj7": [
        {"notes": ("A", "C#", "E", "G#")},
        {"scales": [

            {"scale": "F# minor",
             "notes": ("F#", "A", "B", "C#", "E"),
             "tensions": ("13", "r", "3", "11", "5"),
             "order": 10},

            {"scale": "C# minor",
             "notes": ("C#", "E", "F#", "G#", "B"),
             "tensions": ("3", "5", "13", "7", "9"),
             "order": 20},

            {"scale": "A# minor",
             "notes": ("A#", "C#", "D#", "E#", "G#"),
             "tensions": ("7", "9", "3", "#11", "13"),
             "order": 30},

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
