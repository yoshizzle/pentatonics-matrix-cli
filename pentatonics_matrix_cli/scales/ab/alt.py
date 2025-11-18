# alt.py — Ab key center

SCALE_DATA = {
    "ab7alt": [
        {"notes": ("Ab", "C", "Eb", "E", "Gb", "Bb", "B")},
        {"scales": [

            {"scale": "Ab whole tone",
             "notes": ("Ab", "Bb", "C", "D", "E"),
             "tensions": ("r", "3", "#11", "#5", "b7"),
             "order": 10},

            {"scale": "F major b6",
             "notes": ("Fb", "Ab", "Bb", "C", "Eb"),
             "tensions": ("3", "#5", "b7", "r", "#9"),
             "order": 20},

            {"scale": "Db minor 6",
             "notes": ("Db", "Fb", "Gb", "Ab", "Bb"),
             "tensions": ("b9", "3", "b5", "#5", "7"),
             "order": 30},

            {"scale": "Eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 40},

            {"scale": "Eb minor 6",
             "notes": ("Eb", "Gb", "Ab", "Bb", "C"),
             "tensions": ("#9", "b5", "#5", "b7", "r"),
             "order": 50},

            {"scale": "Bb minor 7b5",
             "notes": ("Bb", "Db", "Eb", "Fb", "Ab"),
             "tensions": ("b7", "b9", "#9", "b5", "#5"),
             "order": 60},

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
