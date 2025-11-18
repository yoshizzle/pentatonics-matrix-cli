# maj7sharp11.py — Eb key center

SCALE_DATA = {
    "ebmaj7#11": [
        {"notes": ("Eb", "G", "Bb", "D", "A")},
        {"scales": [

            {"scale": "c minor 6",
             "notes": ("C", "Eb", "F", "G", "A"),
             "tensions": ("13", "r", "9", "3", "#11"),
             "order": 10},

            {"scale": "d minor",
             "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("7", "9", "3", "#11", "13"),
             "order": 20},

            {"scale": "a whole tone",
             "notes": ("A", "C#", "D#", "F", "G"),
             "tensions": ("#11", "7", "r", "9", "3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Eb", "F", "G", "B", "C#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Eb", "F", "Ab", "Bb", "C"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Eb", "E", "G", "A", "C"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Eb", "Gb", "A", "C", "Db"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
