# dom7nat9flat13.py — Eb key center

SCALE_DATA = {
    "eb7nat9b13": [
        {"notes": ("Eb", "G", "Bb", "Db", "F", "C")},
        {"scales": [

            {"scale": "g whole tone",
             "notes": ("G", "A", "B", "C#", "D#"),
             "tensions": ("3", "13", "b7", "r", "9"),
             "order": 10},

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
