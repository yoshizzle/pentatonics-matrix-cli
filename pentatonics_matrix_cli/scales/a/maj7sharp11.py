# maj7sharp11.py — A key center

SCALE_DATA = {
    "amaj7#11": [
        {"notes": ("A", "C#", "E", "G#", "D#")},
        {"scales": [

            {"scale": "F# minor 6",
             "notes": ("F#", "A", "B", "C#", "D#"),
             "tensions": ("13", "r", "9", "3", "#11"),
             "order": 10},

            {"scale": "C# minor",
             "notes": ("C#", "E", "F#", "G#", "B"),
             "tensions": ("7", "9", "3", "#11", "13"),
             "order": 20},

            {"scale": "F# whole tone",
             "notes": ("F#", "A#", "B#", "D#", "E#"),
             "tensions": ("#11", "7", "r", "9", "3"),
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
