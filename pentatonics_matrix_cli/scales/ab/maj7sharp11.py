# maj7sharp11.py — Ab key center

SCALE_DATA = {
    "abmaj7#11": [
        {"notes": ("Ab", "C", "Eb", "G", "D")},
        {"scales": [

            {"scale": "f minor 6",
             "notes": ("F", "Ab", "Bb", "C", "D"),
             "tensions": ("13", "r", "9", "3", "#11"),
             "order": 10},

            {"scale": "c minor",
             "notes": ("C", "Eb", "F", "G", "Bb"),
             "tensions": ("7", "9", "3", "#11", "13"),
             "order": 20},

            {"scale": "a whole tone",
             "notes": ("A", "C#", "D#", "F", "G"),
             "tensions": ("#11", "7", "r", "9", "3"),
             "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Ab", "Bb", "C", "E", "F"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Ab", "Bb", "Db", "Eb", "F"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Ab", "A", "C", "E", "F"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Ab", "Bb", "C", "Eb", "F#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
