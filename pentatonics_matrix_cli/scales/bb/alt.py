# alt.py — Bb key center

SCALE_DATA = {
    "bb7alt": [
        {"notes": ("Bb", "D", "F", "Gb", "G", "Ab", "C")},
        {"scales": [

            {"scale": "Bb whole tone",
             "notes": ("Bb", "C", "D", "E", "F#"),
             "tensions": ("r", "3", "#11", "#5", "b7"),
             "order": 10},

            {"scale": "F major b6",
             "notes": ("Fb", "Ab", "Bb", "C", "Eb"),
             "tensions": ("3", "#5", "b7", "r", "#9"),
             "order": 20},

            {"scale": "Bb minor 6",
             "notes": ("Bb", "Db", "Eb", "F", "G"),
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
             "notes": ("Bb", "C", "D", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Bb", "C", "Eb", "F", "G"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Bb", "B", "D", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Bb", "C#", "E", "F", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
