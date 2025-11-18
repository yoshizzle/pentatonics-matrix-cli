# alt.py — Eb key center

SCALE_DATA = {
    "eb7alt": [
        {"notes": ("Eb", "G", "A", "Bb", "Db", "E", "Gb")},
        {"scales": [

            {"scale": "eb whole tone",
             "notes": ("Eb", "F", "G", "A", "B"),
             "tensions": ("r", "9", "3", "#11", "#5"),
             "order": 10},

            {"scale": "cb major b6",
             "notes": ("A", "Cb", "Db", "Eb", "Gb"),
             "tensions": ("3", "#5", "b7", "r", "#9"),
             "order": 20},

            {"scale": "f minor 6",
             "notes": ("F", "Ab", "Bb", "C", "D"),
             "tensions": ("#9", "b5", "#5", "b7", "r"),
             "order": 30},

            {"scale": "eb minor 6",
             "notes": ("Eb", "Gb", "Ab", "Bb", "C"),
             "tensions": ("r", "b3", "11", "5", "13"),
             "order": 40},

            {"scale": "bb minor 7b5",
             "notes": ("Bb", "Db", "Eb", "Fb", "Ab"),
             "tensions": ("b7", "b9", "#9", "b5", "#5"),
             "order": 60},

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
