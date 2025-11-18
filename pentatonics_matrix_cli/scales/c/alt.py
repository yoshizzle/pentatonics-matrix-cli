# alt.py

SCALE_DATA = {
    "c7alt": [
        {"notes": ("C", "E", "Gb", "G#", "Bb", "Db", "Eb")},
        {"scales": [
            {"scale": "c whole tone", "notes": ("C", "E", "F#", "G#", "A#"),
             "tensions": ("r", "3", "#11", "#5", "b7"), "order": 10},

            {"scale": "ab major b6", "notes": ("Fb", "Ab", "Bb", "C", "Eb"),
             "tensions": ("3", "#5", "b7", "r", "#9"), "order": 20},

            {"scale": "db minor 6", "notes": ("Db", "Fb", "Gb", "Ab", "Bb"),
             "tensions": ("b9", "3", "b5", "#5", "7"), "order": 30},

            {"scale": "eb minor", "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"), "order": 40},

            {"scale": "eb minor 6", "notes": ("Eb", "Gb", "Ab", "Bb", "C"),
             "tensions": ("#9", "b5", "#5", "b7", "r"), "order": 50},

            {"scale": "bb minor 7b5", "notes": ("Bb", "Db", "Eb", "Fb", "Ab"),
             "tensions": ("b7", "b9", "#9", "b5", "#5"), "order": 60},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "Eb", "G#", "A#"),
             "tensions": ("r", "9", "b3", "#5", "7"), "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C", "D", "F", "G", "Bb"),
             "tensions": ("r", "9", "11", "5", "b7"), "order": 110},

            {"scale": "altered dominant pentatonic",
             "notes": ("C", "Db", "E", "Gb", "Bb"),
             "tensions": ("r", "b9", "3", "b5", "b7"), "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C", "Eb", "Gb", "A", "Bb"),
             "tensions": ("r", "#9", "b5", "13", "b7"), "order": 130}
        ]}
    ]
}
